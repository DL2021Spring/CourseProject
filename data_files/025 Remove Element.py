
__author__ = 'Danyang'
class Solution:
    def removeElement_negative_index(self, A, elem):
        

        open_ptr = 0
        back_ptr = -1  
        while len(A)+back_ptr>=open_ptr:
            if A[open_ptr]==elem:
                A[open_ptr], A[back_ptr] = A[back_ptr], A[open_ptr]
                back_ptr -= 1
            else:
                open_ptr += 1

        return len(A)+back_ptr+1  

    def removeElement(self, A, elem):
        
        open_ptr = 0
        end_ptr = len(A)
        while open_ptr<end_ptr:
            if A[open_ptr]==elem:
                end_ptr -= 1
                A[open_ptr], A[end_ptr] = A[end_ptr], A[open_ptr]
            else:
                open_ptr += 1

        return end_ptr


if __name__=="__main__":
    A = [1, 3, 4, 2, 5, 4]
    elem = 4
    solution = Solution()
    assert solution.removeElement(A, elem)==solution.removeElement_negative_index(A, elem)