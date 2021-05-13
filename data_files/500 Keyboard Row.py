



class Solution:
    def findWords(self, words):
        
        rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
        ]
        d = {
            e: i
            for i, v in enumerate(rows)
            for e in v
        }
        return [
            w
            for w in words
            if all(d[w[0].lower()] == d[l.lower()] for l in w)
        ]


if __name__ == "__main__":
    assert Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]
