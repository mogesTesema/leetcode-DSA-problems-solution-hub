class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        left_g = 0
        left_s = 0
        counter = 0
        while left_g < len(g) and left_s < len(s):
            if g[left_g]<= s[left_s]:
                counter += 1
                left_s +=1
                left_g +=1
            else:
                left_s += 1
        return counter
        


        
