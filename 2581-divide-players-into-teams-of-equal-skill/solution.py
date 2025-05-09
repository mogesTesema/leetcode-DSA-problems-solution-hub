class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        chemistry = 0
        right = len(skill)-1
        totalSkill = skill[left] + skill[right]
        while left < right:
            if skill[left] + skill[right] == totalSkill:
                chemistry += skill[left]*skill[right]
            else:
                return -1
            left += 1
            right -= 1
        return chemistry

            



        
