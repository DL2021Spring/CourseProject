
__author__ = 'Danyang'
class Solution:
    def lengthOfLastWord(self, s):
        
        s = s.strip()
        lst = s.split(" ")
        try:
            last_word = lst[-1]
            return len(last_word)
        except IndexError:
            return 0
