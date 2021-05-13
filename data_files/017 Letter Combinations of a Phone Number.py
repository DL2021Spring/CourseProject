
__author__ = 'Danyang'
class Solution:
    digit2letters = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }

    def letterCombinations(self, digits):
        
        result = []
        self.dfs_traverse(digits, "", result)
        return result

    def dfs_traverse(self, string_seq, current, result):
        if not string_seq:
            result.append(current)
            return

        for letter in self.digit2letters[string_seq[0]]:
            self.dfs_traverse(string_seq[1:], current+letter, result)


if __name__=="__main__":
    print Solution().letterCombinations("23")