from collections import Counter
from typing import List
class Solution:


    def countCharacters(self, words: List[str], chars: str) -> int:
        
        freq_chars = Counter(chars)
        freq_words = []

        for word in words:
            freq_words.append(Counter(word))
        print(freq_chars)
        print(freq_words)

        ans = 0
        for index, word in enumerate(freq_words):
            is_exist = True
            for single_char in word:
                if not (single_char in freq_chars and word[single_char] <= freq_chars[single_char]):
                    is_exist= False
                    break
            if is_exist:
                ans += len(words[index])
        return ans

        
