class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set(['a','e','i','o','u'])
        max_vowels = 0
        current = 0
        s = list(s)
        for i in s[:k]:
            if i in vowel:
                current += 1
        print(current)
        max_vowels = current
        for i in range(k, len(s)):
            if s[i-k] in vowel:
                current -= 1

            if s[i] in vowel:
                current += 1
            max_vowels = max(current,max_vowels)
        return max_vowels

        
