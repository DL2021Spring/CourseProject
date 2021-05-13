

from typing import List


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        
        sentence = " ".join(sentence) + " "  
        i = 0
        for r in range(rows):
            i += cols
            while sentence[i % len(sentence)] != " ":
                i -= 1

            
            i += 1

        ret = i // len(sentence)
        return ret 
