



class Solution:
    def findSubstringInWraproundString(self, p):
        
        counter = {
            c: 1
            for c in p
        }
        l = 1
        for i in range(1, len(p)):
            if (ord(p[i]) - ord(p[i-1])) % 26 == 1:  
                l += 1
            else:
                l = 1
            counter[p[i]] = max(counter[p[i]], l)

        return sum(counter.values())

    def findSubstringInWraproundString_error(self, p):
        
        if not p:
            return 0

        ret = set()
        i = 0
        while i < len(p):
            cur = [p[i]]
            j = i + 1
            while j < len(p) and (ord(p[j]) - ord(cur[-1]) == 1 or p[j] == "a" and cur[-1] == "z"):
                cur.append(p[j])
                j += 1
            ret.add("".join(cur))
            i = j

        return sum(map(lambda x: (len(x) + 1) * len(x) // 2, ret))


if __name__ == "__main__":
    assert Solution().findSubstringInWraproundString("a") == 1
    assert Solution().findSubstringInWraproundString("cac") == 2
    assert Solution().findSubstringInWraproundString("zab") == 6
    assert Solution().findSubstringInWraproundString("zaba") == 6
