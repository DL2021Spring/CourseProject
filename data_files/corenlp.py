



from os import listdir
from os.path import isdir, join as path_join
from re import compile as re_compile, match


from pexpect import spawn


SENTENCE_OUTPUT_REGEX = re_compile(r'Sentence 
OUTPUT_TOKEN_REGEX = re_compile(
    r' CharacterOffsetBegin=(?P<start>[0-9]+).*'
    r' CharacterOffsetEnd=(?P<end>[0-9]+).*'
    r' NamedEntityTag=(?P<type>[^ \]]+)'
    )



class CoreNLPTagger(object):
    def __init__(self, core_nlp_path, mem='1024m'):
        assert isdir(core_nlp_path)
        
        jar_paths = []
        for jar_regex in (
                '^stanford-corenlp-[0-9]{4}-[0-9]{2}-[0-9]{2}\.jar$',
                '^stanford-corenlp-[0-9]{4}-[0-9]{2}-[0-9]{2}-models\.jar$',
                '^joda-time\.jar$',
                '^xom\.jar$',
                ):
            for fname in listdir(core_nlp_path):
                if match(jar_regex, fname):
                    jar_paths.append(path_join(core_nlp_path, fname))
                    break
            else:
                assert False, 'could not locate any jar on the form "%s"' % jar_regex

        
        corenlp_cmd = ' '.join(('java -Xmx%s' % mem,
                '-cp %s' % ':'.join(jar_paths),
                'edu.stanford.nlp.pipeline.StanfordCoreNLP',
                '-annotators tokenize,ssplit,pos,lemma,ner',
                ))

        
        self._core_nlp_process = spawn(corenlp_cmd, timeout=600)
        
        self._core_nlp_process.expect('Entering interactive shell.')

    def __del__(self):
        
        if self._core_nlp_process.isalive():
            self._core_nlp_process.terminate()

    def tag(self, text):
        self._core_nlp_process.sendline(
                
                
                text.replace('\n', ' ')
                )

        
        
        output_timeout = 1 + int(len(text.split()) * 0.5)
        
        self._core_nlp_process.expect(SENTENCE_OUTPUT_REGEX,
                timeout=output_timeout)
        
        self._core_nlp_process.expect('NLP>', timeout=output_timeout)

        annotations = {}
        def _add_ann(start, end, _type):
            annotations[len(annotations)] = {
                    'type': _type,
                    'offsets': ((start, end), ),
                    'texts': ((text[start:end]), ),
                    }

        
        
        for sent_output in (d.strip() for i, d in enumerate(
                self._core_nlp_process.before.rstrip().split('\r\n'))
                if (i + 1) % 3 == 0):
            ann_start = None
            last_end = None
            ann_type = None
            for output_token in sent_output.split('] ['):
                

                
                m = OUTPUT_TOKEN_REGEX.search(output_token)
                assert m is not None, 'failed to parse output'
                

                gdic = m.groupdict()
                start = int(gdic['start'])
                end = int(gdic['end'])
                _type = gdic['type']

                
                if ((_type == 'O' or ann_type != _type)
                        and ann_start is not None):
                    _add_ann(ann_start, last_end, ann_type)
                    ann_start = None
                    ann_type = None
                elif _type != 'O' and ann_start is None:
                    ann_start = start
                    ann_type = _type
                last_end = end
            
            if ann_start is not None:
                _add_ann(ann_start, last_end, ann_type)

        return annotations

if __name__ == '__main__':
    
    tagger = CoreNLPTagger('stanford-corenlp-2012-04-09')
    print tagger.tag('Just a test, like the ones they do at IBM.\n'
            'Or Microsoft for that matter.')
