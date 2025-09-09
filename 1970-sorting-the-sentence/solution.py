class Solution:
    def sortSentence(self, s: str) -> str:
        sent =[ word for word in s.split(" ") ]
        original = [""]*10
        for word in sent:
            if len(word) > 0:
                original[int(word[-1])] = word[:-1]
        print(original)
        ans = " ".join(word for word in original if len(word) > 0)
        return ans
