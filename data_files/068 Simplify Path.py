
__author__ = 'Danyang'


class Solution(object):
    def simplifyPath(self, path):
        
        path = path.split("/")
        path = filter(lambda x: x not in ("", " ", "."), path)

        
        for idx in xrange(len(path)):
            val = path[idx]
            if val == "..":
                path[idx] = "."

                
                i = idx-1
                while i >= 0 and path[i] == ".": i -= 1
                if i >= 0: path[i] = "."  

        path = filter(lambda x: x not in (".",), path)

        if not path:
            return "/"

        path = map(lambda x: "/"+x, path)
        return "".join(path)


if __name__ == "__main__":
    assert Solution().simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///") == "/e/f/g"
    assert Solution().simplifyPath("/a/./b/../../c/") == "/c"
    assert Solution().simplifyPath("/../") == "/