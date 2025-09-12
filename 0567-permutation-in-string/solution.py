from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        
        s1_count = Counter(s1)
        window_count = Counter(s2[:n])  # first window

        if window_count == s1_count:
            return True
        
        for i in range(n, m):
            window_count[s2[i]] += 1          # add new char
            window_count[s2[i - n]] -= 1      # remove old char
            if window_count[s2[i - n]] == 0:  # clean up
                del window_count[s2[i - n]]
            
            if window_count == s1_count:
                return True
        
        return False

