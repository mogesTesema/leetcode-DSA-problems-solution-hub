from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        steps = 0
        for ch in s_count:
            if s_count[ch] > t_count.get(ch, 0):
                steps += s_count[ch] - t_count.get(ch, 0)
        return steps
