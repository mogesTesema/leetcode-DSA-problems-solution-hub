class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, maxLen = 0, 1
        for i in range(n):
            for j in range(2):
                low, high = i, i + j
                while low >= 0 and high < n and s[low] == s[high]:
                    currentLen = high - low + 1
                    if currentLen > maxLen:
                        maxLen = currentLen
                        start = low
                    low -= 1
                    high += 1
        return s[start:start + maxLen]
        
