class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = [word for word in text.split(" ")]
        counter = len(words)
        for word in words:
           
            for letter in word:
                if letter in brokenLetters:
                    counter -= 1
                    break
        return counter


