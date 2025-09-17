from collections import Counter
from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = [words[0]]
        prev = Counter(words[0])

        for i in range(1, len(words)):
            curr = Counter(words[i])
            if curr != prev:  # only append if not an anagram of previous kept word
                ans.append(words[i])
                prev = curr  # update prev to new word's counter
        return ans

