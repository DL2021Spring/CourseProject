
__author__ = 'Danyang'


class Solution:
    def previousPermuation(self, num):
        
        n = len(num)

        partition = n-2
        while partition >= 0 and num[partition] <= num[partition+1]:
            partition -= 1

        if partition < 0:
            return num[::-1]

        change = n-1
        while change >= 0 and num[change] >= num[partition]:
            change -= 1

        num[partition], num[change] = num[change], num[partition]

        
        num[partition+1:] = reversed(num[partition+1:])  
        return num


if __name__ == "__main__":
    print Solution().previousPermuation([1, 3, 2, 3])






