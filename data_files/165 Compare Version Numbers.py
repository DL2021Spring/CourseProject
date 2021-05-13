
__author__ = 'Daniel'


class Solution:
    def compareVersion(self, version1, version2):
        
        version1 = map(int, version1.split("."))
        version2 = map(int, version2.split("."))
        n1 = len(version1)
        n2 = len(version2)

        for i in xrange(min(n1, n2)):
            if version1[i] == version2[i]:
                pass
            else:
                return -1 if version1[i] < version2[i] else 1

        
        if n1 == n2 or n1 > n2 and all(map(lambda x: x == 0, version1[n2:])) or \
                                n1 < n2 and all(map(lambda x: x == 0, version2[n1:])):
            return 0

        return -1 if n1 < n2 else 1

