class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        signs = {")":"(","}":"{","]":"["}
        stack = []
       
        for sign in s:
            if sign  in signs.values():
                stack.append(sign)
            else:
                if stack and signs[sign] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False

    
