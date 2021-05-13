
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        
        A = cipher
        N = len(A)
        start = 0
        while start + 1 < N and A[start] <= A[start + 1]:
            start += 1

        
        end = start + 1
        while end + 1 < N and A[end] >= A[end + 1]:
            end += 1

        if end == start + 1:  
            
            j = start + 1
            while j + 1 < N and A[j] < A[j + 1]:
                j += 1

            
            if j != start + 1 and j + 1 == N:  
                return "no"
            
            i = j + 1
            while i + 1 < N:
                if not A[i] < A[i + 1]:
                    return "no"
                i += 1

            if j != start + 1:
                j += 1
            return "yes\nswap %d %d" % (start + 1, j + 1)
        else:  
            
            i = end + 1
            while i + 1 < N:
                if not A[i] < A[i + 1]:
                    return "no"
                i += 1

            if end + 1 < N and A[start] > A[end + 1]:  
                return "no"

            return "yes\nreverse %d %d" % (start + 1, end + 1)


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())


    
    cipher = map(int, f.readline().strip().split(' '))

    
    s = "%s\n" % (Solution().solve(cipher))
    print s,
