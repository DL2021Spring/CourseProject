



class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        
        if K == 0:
            return 1

        F = [0 for _ in range(N+1)]
        F[0] = 1
        cur_sum = F[0]
        ret = 0
        for i in range(1, N+1):
            F[i] = cur_sum * (1/W)
            if i >= K:
                ret += F[i]
                
            else:
                cur_sum += F[i]
                
            if i - W >= 0:
                cur_sum -= F[i - W]

        return ret

    def new21Game_error(self, N: int, K: int, W: int) -> float:
        
        F = [0 for _ in range(K+W+1)]
        F[0] = 1
        for i in range(1, K+W+1):
            for j in range(W, 0, -1):
                if i - j >= K:
                    break
                if i - j >= 0:
                    F[i] += F[i-j] * 1 / W

        ret = sum(F[1:N+1])  
        print(F, ret)
        return ret


if __name__ == "__main__":
    assert Solution().new21Game(6, 1, 10) == 0.6
