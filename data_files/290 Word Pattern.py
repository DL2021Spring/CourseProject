
__author__ = 'Daniel'


class Solution(object):
    def wordPattern(self, pattern, s):
        lst = s.split(" ")
        if len(pattern) != len(lst):
            return False

        char2word = {}
        words = set()
        for i in xrange(len(pattern)):
            if pattern[i] in char2word:
                if char2word[pattern[i]] != lst[i]:
                    return False
                else:
                    assert lst[i] in words
            else:
                if lst[i] in words:
                    return False
                char2word[pattern[i]] = lst[i]
                words.add(lst[i])

        return True


class OneToOneMap(object):
    def __init__(self):
        self.m = {}  

    def set(self, a, b):
        self.m[a] = b
        self.m[b] = a

    def get(self, a):
        return self.m.get(a)


class SolutionError(object):
    def wordPattern(self, pattern, str):
        
        m = OneToOneMap()
        lst = str.split(" ")
        if len(pattern) != len(lst):
            return False

        for i in xrange(len(pattern)):
            a = m.get(pattern[i])
            b = m.get(lst[i])
            if a is None and b is None:
                m.set(pattern[i], lst[i])
            elif a is None and b is not None:
                return False
            elif a != lst[i]:
                return False

        return True


if __name__ == "__main__":
    assert Solution().wordPattern("abba", "dog cat cat dog") == True
