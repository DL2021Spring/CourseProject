
__author__ = 'Danyang'
class Solution:
    def getRow(self, rowIndex):
        
        if rowIndex<0:
            return None
        if rowIndex==0:
            return [1]

        current_level = [1, 1]
        for row in xrange(2, rowIndex+1):

            
            temp = current_level[0]
            for col in xrange(1, row): 
                summation = current_level[col] + temp
                temp = current_level[col]
                current_level[col] = summation

            current_level.append(1)

        return current_level


if __name__=="__main__":
    print Solution().getRow(3)