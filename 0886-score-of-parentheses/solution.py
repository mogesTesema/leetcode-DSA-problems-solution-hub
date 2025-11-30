class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for sign in s:
            if sign == "(":
                stack.append(0)
            else:
                curr_sum = 0
                while stack[-1] != 0:
                    curr_sum += stack.pop() 
                val = max(curr_sum*2,1)
                stack.pop()
                stack.append(val)
                
        return sum(stack)

