

from typing import List
from collections import defaultdict


class Node:
    def __init__(self, chr):
        self.chr = chr
        self.ended = False
        self.children = defaultdict(lambda: None)


class Trie:
    def __init__(self):
        self.root = Node(None)  

    @classmethod
    def insert(cls, node, w, i):
        if not node:
            node = Node(w[i])

        if i == len(w) - 1:
            node.ended = True
        else:
            nxt = w[i + 1]
            node.children[nxt] = cls.insert(node.children[nxt], w, i + 1)

        return node

    @classmethod
    def search(cls, node, w, i):
        if not node:
            return

        if node.chr != w[i]:
            return

        if node.ended:
            return w[:i+1]
        elif i + 1 < len(w):
            return cls.search(node.children[w[i + 1]], w, i + 1)
        else:
            return

class Solution:
    def replaceWords(self, dic: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dic:
            root = trie.root
            root.children[word[0]] = Trie.insert(root.children[word[0]], word, 0)

        ret = []
        for word in sentence.split(" "):
            for child in trie.root.children.values():
                searched = Trie.search(child, word, 0)
                if searched:
                    ret.append(searched)
                    break
            else:
                ret.append(word)

        return " ".join(ret)


if __name__ == "__main__":
    assert Solution().replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery") == "the cat was rat by the bat"
