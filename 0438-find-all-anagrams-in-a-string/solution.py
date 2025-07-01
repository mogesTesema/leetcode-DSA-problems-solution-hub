from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        ans = []
        target = dict()
        for char_p in p:
            target[char_p] = target.get(char_p, 0) + 1
        
        current = dict()
        if len(p)>len(s):
            return ans
        for i in range(len(p)):
            current[s[i]] = current.get(s[i], 0) + 1
            
        for right in range(len(p), len(s) + 1):
            if current == target:
                ans.append(left)
            
            if right < len(s):
                current[s[left]] -= 1
                if current[s[left]] == 0:
                    del current[s[left]]
                
                current[s[right]] = current.get(s[right], 0) + 1
            
            left += 1
            
        return ans
