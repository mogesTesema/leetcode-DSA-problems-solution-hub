class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        t_count = Counter(t)
        s_count = Counter(s)

        if len(t_count) != len(s_count):
            return False
        for key,val in t_count.items():
            if key not in s_count:
                return False
            if s_count[key] != val:
                return False

        return True
        
