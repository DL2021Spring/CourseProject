



class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        n = len(s)
        i = 0
        j = n - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                
                
                return self.is_palindrome(s[i:j]) or self.is_palindrome(s[i+1:j+1])

        return True

    def is_palindrome(self, s):
        return s == s[::-1]


if __name__ == "__main__":
    assert Solution().validPalindrome("aba") == True
    assert Solution().validPalindrome("abca") == True
