import os
import subprocess
import sys 

class CVSHandler():
    
    def __init__(self, cvs):
        self._roots_cache = {}
        self._not_tracked_cache = set()
        self.cvs = cvs

    def _get_root_from_cache(self, directory):
        
        if directory in self._roots_cache:
            return directory
        if os.path.dirname(directory) == directory:
            return None
        return self._get_root_from_cache(os.path.dirname(directory))

    def get_source_files(self, directory):
        if directory in self._not_tracked_cache:
            return None

        root_dir = self._get_root_from_cache(directory)
        if not root_dir:
            try:
                
                root_dir = self.cvs._get_root(directory)
                self._roots_cache[root_dir] = self.cvs._get_tracked_files(root_dir)
            except Exception as e:
                
                self._not_tracked_cache.add(directory)
                return None

        files = self._roots_cache[root_dir]
        
        if directory != root_dir:
            rel_dir = os.path.relpath(directory, root_dir)
            files = [f[len(rel_dir)+1:] for f in files if f.startswith(rel_dir)]
        return files
 

class Git():
    @staticmethod
    def _get_root(directory):
        return run_command("cd %s && git rev-parse --show-toplevel" % directory).strip()
    @staticmethod
    def _get_tracked_files(directory):
        return run_command("cd %s && git ls-files && git ls-files --others --exclude-standard" % directory).strip().split('\n')

class Mercurial():
    @staticmethod
    def _get_root(directory):
        return run_command("cd %s && hg root" % directory).strip()
    @staticmethod
    def _get_tracked_files(directory):
        return run_command("cd %s && (hg status -marcu | cut -d' ' -f2)" % directory).strip().split('\n')

class DefaultDirHandler():
    

    def __init__(self):
        self._cache = {}
        self.MAX_DEPTH = 3

    def _walk_down(self, start_dir):
        try:
            out = run_command("find %s -maxdepth %s -type f -not -path '*/\.*'" % (start_dir, self.MAX_DEPTH))
        except subprocess.CalledProcessError as e:
            
            
            out = e.output
            if sys.version_info >= (3, 0):
                out = out.decode('utf-8')
        if not out:
            return []
        files = out.split('\n')
        return [os.path.relpath(f, start_dir) for f in files if f]

    def get_source_files(self, start_dir):
        if not start_dir in self._cache:
            self._cache[start_dir] = self._walk_down(start_dir)
        return self._cache[start_dir]

def run_command(string):
    
    DEVNULL = open(os.devnull, 'wb')
    out = subprocess.check_output(string, stderr=DEVNULL, shell=True)
    if sys.version_info >= (3, 0):
        return out.decode('utf-8')
    return out


git = CVSHandler(Git)
hg = CVSHandler(Mercurial)
default = DefaultDirHandler()

def get_source_files(directory):
    
    files = git.get_source_files(directory)
    
    if files:
        return files
    files = hg.get_source_files(directory)
    if files:
        return files
    return default.get_source_files(directory)

