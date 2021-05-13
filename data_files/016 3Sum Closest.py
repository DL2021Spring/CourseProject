
__author__ = 'Danyang'
class Solution:
    def threeSumClosest(self, num, target):
        
        min_distance = 1<<32
        num.sort()
        min_summation = 0

        for i, val in enumerate(num):
            j = i+1
            k = len(num)-1
            while j<k:
                lst = [val, num[j], num[k]]
                if min_distance>abs(target-sum(lst)):
                    min_summation = sum(lst)
                    if sum(lst)==target:
                        return min_summation
                    min_distance = abs(target-min_summation)
                elif sum(lst)>target:
                    k -= 1
                else:
                    j += 1
        return min_summation

if __name__=="__main__":
    print Solution().threeSumClosest([1, 1, 1, 1], 0)

