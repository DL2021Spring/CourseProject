

from typing import List


MAX = 2 ** 31 - 1


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        
        l = len(S)
        for i in range(1, l + 1):
            num_str = S[:i]
            if len(num_str) > 1 and num_str.startswith("0"):
                continue

            num = int(num_str)
            if num > MAX:
                break

            for j in range(i + 1, l + 1):
                num2_str = S[i:j]
                if len(num2_str) > 1 and num2_str.startswith("0"):
                    continue

                num2 = int(num2_str)
                if num2 > MAX:
                    break

                ret = [num, num2]
                k = j
                while k < l:
                    nxt = ret[-1] + ret[-2]
                    if nxt > MAX:
                        break

                    nxt_str = str(nxt)
                    if S[k:k+len(nxt_str)] == nxt_str:
                        k = k + len(nxt_str)
                        ret.append(nxt)
                    else:
                        break
                else:
                    if k == l and len(ret) >= 3:
                        return ret

        return []


if __name__ == "__main__":
    assert Solution().splitIntoFibonacci("123456579") == [123,456,579]
    assert Solution().splitIntoFibonacci("01123581321345589") == [0,1,1,2,3,5,8,13,21,34,55,89]
