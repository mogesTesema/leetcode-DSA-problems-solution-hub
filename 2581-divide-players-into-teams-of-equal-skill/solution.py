class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) -1
        if len(skill)>=2:
            team = skill[0]+skill[-1]
        cem = 0
        while left < right:

            curr_team = skill[left]+skill[right]
            if curr_team != team:
                return -1
            cem += skill[left]*skill[right]
            left += 1
            right -= 1
        return cem


