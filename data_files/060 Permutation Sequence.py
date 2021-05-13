
import math

__author__ = 'Danyang'


class Solution(object):
    def getPermutation(self, n, k):
        k -= 1

        array = range(1, n+1)
        k %= math.factorial(n)
        ret = []
        for i in xrange(n-1, -1, -1):
            idx, k = divmod(k, math.factorial(i))
            ret.append(array.pop(idx))

        return "".join(map(str, ret))

    def getPermutation(self, n, k):
        
        
        fac = [1 for _ in xrange(n)]
        for i in xrange(1, n):
            fac[i] = fac[i-1]*i

        
        k -= 1  
        a = [0 for _ in xrange(n)]
        for i in xrange(n-1, -1, -1):
            a[n-1-i] = k/fac[i]  
            k %= fac[i]

        
        candidate = range(1, n+1)  
        visited = [False for _ in xrange(n)]
        for ind, val in enumerate(a):
            i = 0  
            cnt = 0  
            while True:
                if visited[i]:
                    i += 1
                else:
                    if cnt == val: break
                    cnt += 1
                    i += 1

            a[ind] = candidate[i]
            visited[i] = True

        return "".join(map(str, a))

    def getPermutation_complicated(self, n, k):
        
        k -= 1  

        factorial = 1  
        for i in xrange(1, n):
            factorial *= i

        result = []
        array = range(1, n+1)
        for i in reversed(xrange(1, n)):
            index = k/factorial
            result.append(array[index])
            array = array[:index]+array[index+1:]
            k = k%factorial
            factorial /= i

        
        result.append(array[0])

        return "".join(str(element) for element in result)


class Solution_TLE:
    

    def __init__(self):
        self.counter = 0

    def getPermutation(self, n, k):
        
        if not n:
            return

        sequence = range(1, n+1)
        result = self.get_kth_permutation_dfs(sequence, k, [])
        return "".join(str(element) for element in result)


    def get_kth_permutation_dfs(self, remaining_seq, k, cur):
        
        if not remaining_seq:
            self.counter += 1
            if self.counter == k:
                return cur

        for ind, val in enumerate(remaining_seq):
            result = self.get_kth_permutation_dfs(remaining_seq[:ind]+remaining_seq[ind+1:], k, cur+[val])
            if result: return result


if __name__ == "__main__":
    assert Solution().getPermutation(4, 6) == "1432"
    assert Solution().getPermutation(2, 2) == "21"
    assert Solution().getPermutation(3, 1) == "123"
    assert Solution().getPermutation(3, 5) == "312"
    print Solution().getPermutation(9, 171669)