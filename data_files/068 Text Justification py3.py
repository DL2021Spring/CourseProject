

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        ret = []
        char_cnt = 0  
        cur_words = []

        for w in words:
            cur_words.append(w)
            char_cnt += len(w)
            if char_cnt + len(cur_words) - 1 > maxWidth:
                
                cur_words.pop()
                char_cnt -= len(w)
                for i in range(maxWidth - char_cnt):
                    cur_words[i % max(1, len(cur_words) - 1)] += " "

                ret.append("".join(cur_words))

                cur_words = [w]
                char_cnt = len(w)

        
        last = " ".join(cur_words)
        ret.append(last + " " * (maxWidth - len(last)))
        return ret


class Solution2:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        ret = []
        char_cnt = 0
        cur_words = []

        for w in words:
            
            if char_cnt + len(w) + len(cur_words) > maxWidth:
                
                
                for i in range(maxWidth - char_cnt):
                    cur_words[i % max(1, len(cur_words) - 1)] += " "  
                    
                ret.append("".join(cur_words))

                cur_words = []
                char_cnt = 0

            cur_words.append(w)
            char_cnt += len(w)

        
        last = " ".join(cur_words)
        ret.append(last + " " * (maxWidth - len(last)))
        return ret


if __name__ == "__main__":
    assert Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16) == ["This    is    an","example  of text","justification.  "]
    assert Solution().fullJustify(["What","must","be","acknowledgment","shall","be"], 16) == ["What   must   be","acknowledgment  ","shall be        "]
