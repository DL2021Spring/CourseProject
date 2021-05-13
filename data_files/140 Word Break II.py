
__author__ = 'Danyang'
from collections import deque


class Solution:
    def wordBreak(self, s, dict):
        
        
        dp = [[] for _ in range(len(s) + 1)]

        dp[0].append("dummy")

        for i in range(len(s)):
            if not dp[i]:
                continue

            for word in dict:
                if s[i:i + len(word)] == word:
                    dp[i + len(word)].append(word)

        
        if not dp[-1]:
            return []

        result = []
        self.build_result(dp, len(s), deque(), result)
        return result


    def build_result(self, dp, cur_index, cur_sentence, result):
        
        
        if cur_index == 0:
            result.append(" ".join(cur_sentence))
            return

        
        for prefix in dp[cur_index]:
            cur_sentence.appendleft(prefix)
            self.build_result(dp, cur_index - len(prefix), cur_sentence, result)
            cur_sentence.popleft()


if __name__=="__main__":
    assert Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])==['cat sand dog', 'cats and dog']
