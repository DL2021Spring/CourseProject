



class Solution:
    def findComplement(self, num):
        
        msb = 0
        while num >> msb:
            msb += 1

        mask = (1 << msb) - 1
        return mask & ~num


if __name__ == "__main__":
    assert Solution().findComplement(5) == 2
