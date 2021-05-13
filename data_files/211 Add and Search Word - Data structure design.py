
__author__ = 'Daniel'


class TrieNode:
    def __init__(self):
        
        
        self.ended = False
        self.children = {}


class WordDictionary:
    def __init__(self):
        
        self.root = TrieNode()

    def addWord(self, word):
        
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]

        cur.ended = True

    def search(self, word):
        
        return self.__search(word, self.root)

    def __search(self, word, cur):
        if not word:
            return cur.ended

        w = word[0]
        if w != ".":
            if w in cur.children:
                return self.__search(word[1:], cur.children[w])
            else:
                return False
        else:
            for child in cur.children.values():
                if self.__search(word[1:], child):
                    return True

        return False

if __name__ == "__main__":
    dic = WordDictionary()
    dic.addWord("a")
    assert dic.search(".") == True