class Solution:
    def isValid(self, s: str) -> bool:
        pair = {")":"(","}":"{","]":"["}

        stack = []

        for s in s:
            if s in pair and len(stack)> 0:
                if pair[s] == stack[-1]:
                    stack.pop()
                else:
                    return False
            elif s in pair and len(stack) == 0:
                return False
            else:
                stack.append(s)
        return True if len(stack) == 0 else False
