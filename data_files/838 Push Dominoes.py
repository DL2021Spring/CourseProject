



class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        n = len(dominoes)
        L = [float("inf") for i in range(n)]
        R = [float("inf") for i in range(n)]
        for i in range(n-1, -1, -1):
            if dominoes[i] == "L":
                L[i] = 0
            elif dominoes[i] == "R":
                L[i] = float("inf")
            elif i + 1 < n:
                L[i] = L[i+1] + 1

        for i in range(n):
            if dominoes[i] == "R":
                R[i] = 0
            elif dominoes[i] == "L":
                R[i] = float("inf")
            elif i - 1 >= 0:
                R[i] = R[i-1] + 1

        ret = []
        for i in range(n):
            d = min(R[i], L[i])
            if d == float("inf"):
                cur = "."
            elif R[i] == L[i]:
                cur = "."
            elif d == R[i]:
                cur = "R"
            else:
                cur = "L"
            ret.append(cur)

        return "".join(ret)


if __name__ == "__main__":
    assert Solution().pushDominoes(".L.R...LR..L..") == "LL.RR.LLRRLL.."
