
__author__ = 'Danyang'
class Solution:
    def combinationSum(self, candidates, target):
        
        candidates.sort()
        result = []
        self.get_combination(target, candidates, [], result)
        return result

    def get_combination(self, target, candidates, current, result):
        if not candidates or sum(current)>target:
            return
        if sum(current)==target:
            result.append(current)
            return

        
        for ind, val in enumerate(candidates):
            self.get_combination(target, candidates[ind:], current+[val], result)  



if __name__=="__main__":
    print Solution().combinationSum([2,3,6,7], 7)