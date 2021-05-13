



class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        seq = list(str(n))
        N = len(seq)
        if N < 2:
            return -1

        
        i = N - 2
        while seq[i] >= seq[i+1]:
            i -= 1
            if i < 0:
                return -1

        j = N - 1
        while seq[i] >= seq[j]:
            j -= 1

        seq[i], seq[j] = seq[j], seq[i]
        seq[i+1:] = reversed(seq[i+1:])
        ret = int("".join(seq))
        if ret <= 1 << 31 - 1:
            return ret
        else:
            return -1

    def nextGreaterElement_sort(self, n: int) -> int:
        
        seq = [int(e) for e in str(n)]
        stk = []  
        for i in range(len(seq) - 1, -1 , -1):
            e = seq[i]
            popped = None
            while stk and seq[stk[-1]] > e:
                popped = stk.pop()

            if popped:
                seq[i], seq[popped] = seq[popped], seq[i]
                seq[i+1:] = sorted(seq[i+1:])  
                ret = int("".join(map(str, seq)))
                if ret <= 1 << 31 - 1:
                    return ret
                else:
                    return -1

            stk.append(i)

        return -1


if __name__ == "__main__":
    assert Solution().nextGreaterElement(12) == 21
