

from collections import defaultdict


class Solution:
    def findLongestWord(self, s, d):
        
        h = defaultdict(list)
        for d_idx, w in enumerate(d):
            w_idx = 0
            h[w[w_idx]].append((d_idx, w_idx))

        ret = ""
        for e in s:
            lst = h.pop(e, [])
            for d_idx, w_idx in lst:
                w = d[d_idx]
                w_idx += 1
                if w_idx >= len(w):
                    
                    ret = min(ret, w, key=lambda x: (-len(x), x))  
                else:
                    h[w[w_idx]].append((d_idx, w_idx))

        return ret


if __name__ == "__main__":
    assert Solution().findLongestWord("abpcplea", ["ale","apple","monkey","plea"]) == "apple"
