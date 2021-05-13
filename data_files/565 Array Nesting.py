

from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        visited = set()
        ret = 0
        for n in nums:
            count = self.dfs(nums, n, set(), visited)
            ret = max(ret, count)

        return ret

    def dfs(self, nums, num, path, visited):
        if num in visited:
            return 0

        visited.add(num)
        path.add(num)  
        self.dfs(nums, nums[num], path, visited)
        return len(path)


if __name__ == "__main__":
    assert Solution().arrayNesting([5,4,0,3,1,6,2]) == 4
