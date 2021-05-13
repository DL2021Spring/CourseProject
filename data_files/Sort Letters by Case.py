
__author__ = 'Danyang'


class Solution:
    def sortLetters(self, chars):
        
        closed = -1
        for ind, val in enumerate(chars):
            if ord(val) < ord('a'):  
                continue
            else:
                closed += 1
                chars[ind], chars[closed] = chars[closed], chars[ind]


if __name__ == "__main__":
    chars = list("abAcD")
    Solution().sortLetters(chars)
    assert "".join(chars) == "abcAD