

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        F: List[List[str]] = [[] for _ in range(n + 1)]
        F[0].append("")
        for i in range(1, n+1):
            for j in range(i):
                for s1 in F[j]:
                    for s2 in F[i-j-1]:
                        F[i].append(f"({s1}){s2}")

        return F[n]
