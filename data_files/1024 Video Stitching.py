

from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        
        clips.sort()
        prev_e = 0
        ret = 0

        i = 0
        while i < len(clips):
            if clips[i][0] > prev_e:  
                break

            max_e = -float("inf")
            while i < len(clips) and clips[i][0] <= prev_e:
                max_e = max(max_e, clips[i][1])
                i += 1

            prev_e = max_e  
            ret += 1
            if prev_e >= T:
                break

        return ret if prev_e >= T else -1

    def videoStitching_error(self, clips: List[List[int]], T: int) -> int:
        
        A = [(s, -e, s, e) for s, e in clips]
        A.sort()
        ret = 1
        _, _, prev_s, prev_e = A[0]
        if prev_s > 0:
            return False

        for _, _, s, e in A[1:]:
            if s <= prev_e and e > prev_e:
                prev_e = e
                ret += 1


if __name__ == "__main__":
    assert Solution().videoStitching([[0,4],[2,8]], 5) == 2
