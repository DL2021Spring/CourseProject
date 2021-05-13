



class Solution:
    def is_neighbor(self, p, q):
        diff = 0
        for a, b in zip(p, q):
            if a != b:
                diff += 1
            if diff > 1:
                return False
        return True

    def minMutation(self, start, end, bank):
        
        q = [start]
        visited = {start}
        lvl = 0
        while q:
            cur_q = []
            for e in q:
                if e == end:
                    return lvl
                for t in bank:
                    if t not in visited and self.is_neighbor(e, t):
                        visited.add(t)
                        cur_q.append(t)

            lvl += 1
            q = cur_q

        return -1


if __name__ == "__main__":
    assert Solution().minMutation("AACCTTGG", "AATTCCGG", ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]) == -1
    assert Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]) == 2
