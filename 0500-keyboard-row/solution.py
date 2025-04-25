class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = "qwertyuiop"
        second = "asdfghjkl"
        thrid = "zxcvbnm"
        ans = []
        for word in words:
            word2= word.lower()
            word2 = set(word2)
            test1 = True
            test2 = True
            test3 = True
            for wrd in word2:
                if not wrd in first:
                    test1 = False
                if not wrd in second:
                    test2 = False
                if not wrd in thrid:
                    test3 = False
            if test1 or test2 or test3:
                ans.append(word)
                
        return ans
