



class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        
        n = len(S)
        Z = [0 for _ in range(n+1)]  
        O = [0 for _ in range(n+1)]  
        for i in range(1, n+1):
            O[i] = O[i-1]
            if S[i-1] == "1":
                O[i] += 1

        for i in range(n-1, -1, -1):
            Z[i] = Z[i+1]
            if S[i] == "0":
                Z[i] += 1

        ret = float('inf')
        for i in range(n):
            ret = min(ret, O[i] + Z[i+1])

        return ret
