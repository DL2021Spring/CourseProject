

from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        
        mini, maxa = 0, len(S)
        ret = []
        for c in S:
            if c == "I":
                ret.append(mini)
                mini += 1
            else:  
                ret.append(maxa)
                maxa -= 1

        ret.append(mini)
        return ret

    def diStringMatchErrror(self, S: str) -> List[int]:
        
        ret = [0]
        for c in S:
            if c == "I":
                ret.append(ret[-1] + 1)
            else:
                ret.append(ret[-1] -1)
        mn = min(ret)
        return [
            e - mn
            for e in ret
        ]
