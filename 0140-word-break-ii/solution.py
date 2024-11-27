class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = TrieNode()
        for w in wordDict:
            root.addWord(w)

        res = []
        
        def dfs(i, node, word, a, flag=False):
            if i == len(s):
                if flag:
                    res.append(" ".join(a))
                return 
            
            if s[i] not in node.children:
                return 

            word += s[i]
            node = node.children[s[i]]
            
            if node.word:
                a1 = copy.copy(a)
                a1.append(word)
                dfs(i + 1, root, '', a1, flag=True)

            dfs(i + 1, node, word, a)

        dfs(0, root, '', [])
        return res
