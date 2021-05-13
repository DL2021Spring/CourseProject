



class Solution:
    def minMoves(self, nums):
        
        mini = min(nums)
        return sum(map(lambda e: e - mini, nums))


if __name__ == "__main__":
    assert Solution().minMoves([1, 2, 3]) == 3
