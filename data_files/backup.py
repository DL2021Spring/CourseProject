



from datetime import datetime
from os import mkdir, remove
from os.path import dirname, exists, basename
from os.path import join as path_join
from shlex import split as shlex_split
from subprocess import Popen
from sys import path as sys_path
from sys import stderr as sys_stderr

sys_path.append(path_join(dirname(__file__), '..'))

from config import WORK_DIR, DATA_DIR


TOOL_BACKUP_DIR = path_join(WORK_DIR, 'bckup_tool')


def _safe_dirname(path):
    
    return basename(path) or dirname(dirname(path))

def main(args):
    if not exists(TOOL_BACKUP_DIR):
        mkdir(TOOL_BACKUP_DIR)

    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M%SZ')
    backup_path = path_join(TOOL_BACKUP_DIR, '%s-%s.tar.gz' % (
        _safe_dirname(DATA_DIR), timestamp))
    data_dir_parent = path_join(DATA_DIR, '..')

    tar_cmd = 'tar -c -z -f %s -C %s %s' % (backup_path, data_dir_parent,
            _safe_dirname(DATA_DIR))
    tar_p = Popen(shlex_split(tar_cmd))
    tar_p.wait()

    if tar_p.returncode != 0:
        
        remove(backup_path)
        return -1
    else:
        return 0

if __name__ == '__main__':
    from sys import argv
    exit(main(argv))
