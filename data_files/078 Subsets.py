
__author__ = 'Danyang'
class Solution:
    def subsets(self, S):
        
        S.sort()
        result = []
        self.generate_subsets(S, [], result)
        return result

    def generate_subsets(self, S, current, result):
        result.append(current)
        for ind, val in enumerate(S):
            self.generate_subsets(S[ind+1:], current+[val], result)

if __name__=="__main__":
    print Solution().subsets([1, 2, 3])