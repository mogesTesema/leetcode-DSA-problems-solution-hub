class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        content = 0
        child_pointer = 0
        cookie_pointer = 0
        while child_pointer < len(g) and cookie_pointer < len(s):
            if s[cookie_pointer] >= g[child_pointer]:
                content += 1
                cookie_pointer += 1
                child_pointer += 1
            else:
                cookie_pointer += 1
        return content
