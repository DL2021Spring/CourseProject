



class Solution:
    def findDisappearedNumbers(self, A):
        
        for idx in range(len(A)):
            while True:
                target = A[idx] - 1
                if idx == target or A[idx] == A[target]:
                    break 
                A[idx], A[target] = A[target], A[idx]

        missing = []
        for idx, elm in enumerate(A):
            if idx != elm - 1:
                missing.append(idx + 1)
        return missing


if __name__ == "__main__":
    assert Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
