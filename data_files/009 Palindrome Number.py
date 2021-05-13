
__author__ = 'Danyang'


class Solution:
    def isPalindrome(self, x):
        
        if x < 0:
            return False

        
        div = 1
        while x/div >= 10:
            div *= 10  

        while x > 0:
            msb = x/div
            lsb = x%10

            if msb != lsb:
                return False

            
            x %= div
            x /= 10

            div /= 100

        return True


if __name__ == "__main__":
    Solution().isPalindrome(2147483647)