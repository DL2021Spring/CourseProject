



import sys
from os.path import join as path_join
from os.path import dirname


from sys import path as sys_path
sys_path.append(path_join(dirname(__file__), '../server/src'))

from ssplit import regex_sentence_boundary_gen

def _text_by_offsets_gen(text, offsets):
    for start, end in offsets:
        yield text[start:end]

def _normspace(s):
    import re
    return re.sub(r'\s', ' ', s)

def sentencebreaks_to_newlines(text):
    line_offset = 1
    if "\r\n" in text:
        line_offset = 2
    offsets = [o for o in regex_sentence_boundary_gen(text)]

    
    sentences = [s for s in _text_by_offsets_gen(text, offsets)]

    
    orig_parts = []
    new_parts = []

    sentnum = len(sentences)
    for i in range(sentnum):
        sent = sentences[i]
        orig_parts.append(sent)
        new_parts.append(sent)

        if i < sentnum-1:
            orig_parts.append(text[offsets[i][1]:offsets[i+1][0]])

            if (offsets[i][1] < offsets[i+1][0] and
                text[offsets[i][1]].isspace()):
                
                new_parts.append('\n'+text[offsets[i][1]+line_offset:offsets[i+1][0]])
            else:
                new_parts.append(text[offsets[i][1]:offsets[i+1][0]])

    if len(offsets) and offsets[-1][1] < len(text):
        orig_parts.append(text[offsets[-1][1]:])
        new_parts.append(text[offsets[-1][1]:])

    
    assert text == ''.join(orig_parts), "INTERNAL ERROR:\n    '%s'\nvs\n    '%s'" % (text, ''.join(orig_parts))

    splittext = ''.join(new_parts)

    
    assert len(text) == len(splittext), "INTERNAL ERROR"
    assert _normspace(text) == _normspace(splittext), "INTERNAL ERROR:\n    '%s'\nvs\n    '%s'" % (_normspace(text), _normspace(splittext))

    return splittext

def main(argv):
    while True:        
        text = sys.stdin.readline()
        if len(text) == 0:
            break
        sys.stdout.write(sentencebreaks_to_newlines(text))

if __name__ == "__main__":
    sys.exit(main(sys.argv))
