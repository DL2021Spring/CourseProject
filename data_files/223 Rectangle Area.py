
__author__ = 'Daniel'


class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        
        S_A = (C-A)*(D-B)
        S_B = (G-E)*(H-F)

        l = max(0, min(C, G)-max(A, E))
        h = max(0, min(D, H)-max(B, F))
        return S_A + S_B - l*h


if __name__ == "__main__":
    assert Solution().computeArea(-2, -2, 2, 2, -2, -2, 2, 2) == 16