
__author__ = 'Danyang'


class Solution:
    def nextPermutation(self, num):
        
        length = len(num)

        partition_num_index = 0
        change_num_index = 0

        for i in reversed(xrange(1, length)):
            if num[i]>num[i-1]:
                partition_num_index = i-1
                break
        for i in reversed(xrange(1, length)):
            if num[i]>num[partition_num_index]:
                change_num_index = i
                break

        num[partition_num_index], num[change_num_index] = num[change_num_index], num[partition_num_index]

        if partition_num_index==change_num_index==0:
            
            num.reverse()
        else:
            num[partition_num_index+1:] = reversed(num[partition_num_index+1:])
        return num


if __name__=="__main__":
    print Solution().nextPermutation([3, 2, 1])
