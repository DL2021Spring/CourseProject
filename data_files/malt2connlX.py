



from sys import stdin, stdout
from re import compile as _compile
from codecs import open as _open


MALT_REGEX = _compile(ur'^(?P<token>.*?)\t(?P<pos>[^\t]+)\t'
        ur'(?P<head>[^\t]+)\t(?P<rel>[^\t]+)$')

OUTPUT_LINE = u'{token_num}\t{token}\t_\t{pos}\t{pos}\t_\t{head}\t{rel}\t_\t_'


def main(args):
    token_cnt = 0
    for line in (l.decode('utf-8').rstrip('\n') for l in stdin):
        if not line:
            
            token_cnt = 0
            stdout.write('\n')
            continue
        else:
            token_cnt += 1

        m = MALT_REGEX.match(line)
        assert m is not None, 'parse error (sorry...)'
        g_dic = m.groupdict()
        output = OUTPUT_LINE.format(
                token_num=token_cnt,
                token=g_dic['token'],
                pos=g_dic['pos'],
                head=g_dic['head'],
                rel=g_dic['rel']
                )
        stdout.write(output.encode('utf-8'))
        stdout.write('\n')

if __name__ == '__main__':
    from sys import argv
    exit(main(argv))
