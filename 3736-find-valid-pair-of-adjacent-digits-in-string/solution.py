class Solution:
    def findValidPair(self, s: str) -> str:
        pair_freq = Counter(s)

        for i in range(len(s)-1):
            first_str = s[i]
            second_str = s[i+1]
            if first_str != second_str:
                if int(first_str) == pair_freq[first_str] and int(second_str) == pair_freq[second_str]:
                    return first_str + second_str
        return ""
        
