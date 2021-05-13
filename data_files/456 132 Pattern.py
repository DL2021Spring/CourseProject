



class Solution:
    def find132pattern(self, nums):
        
        stack = []  
        mini = float('Inf')
        for v in nums:
            while stack and stack[-1][1] <= v:  
                stack.pop()
            if stack and stack[-1][0] < v:
                return True
            mini = min(mini, v)
            stack.append((mini, v))

        return False


    def find132pattern_TLE(self, nums):
        
        for i in range(len(nums)):
            maxa = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    if nums[j] < maxa:
                        return True
                    maxa = max(maxa, nums[j])

        return False


if __name__ == "__main__":
    assert Solution().find132pattern([1, 2, 3, 4]) == False
    assert Solution().find132pattern([3, 1, 4, 2]) == True
    assert Solution().find132pattern([-1, 3, 2, 0]) == True
    assert Solution().find132pattern([-2, 1, 1]) == True
