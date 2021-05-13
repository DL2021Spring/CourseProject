
__author__ = 'Danyang'


class Solution(object):
    def searchMatrix(self, mat, target):
        
        if not mat:
            return False

        m = len(mat)
        n = len(mat[0])

        
        lo = 0
        hi = m  
        while lo < hi:
            mid = (lo+hi)/2
            if mat[mid][0] == target:
                return True
            elif mat[mid][0] < target:
                lo = mid+1
            else:
                hi = mid

        lst = mat[lo-1]  

        
        lo = 0
        hi = n  
        while lo < hi:
            mid = (lo+hi)/2
            if lst[mid] == target:
                return True
            elif lst[mid] < target:
                lo = mid+1
            else:
                hi = mid

        return False


if __name__ == "__main__":
    assert Solution().searchMatrix([[1], [3]], 3) == True