
__author__ = 'Danyang'
class Solution:
    def canCompleteCircuit(self, gas, cost):
        
        length = len(gas)

        
        diff = [gas[i]-cost[i] for i in xrange(length)]

        
        
        if sum(diff)<0:
            return -1

        
        start_index = 0
        sum_before = 0
        for ind, val in enumerate(diff):  
            sum_before += val
            if sum_before<0:  
                start_index = ind+1
                sum_before = 0

        return start_index

if __name__=="__main__":
    Solution().canCompleteCircuit([5], [4])