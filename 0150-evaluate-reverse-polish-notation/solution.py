class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        polish_stack = []
        for token in tokens:
            if token == "+":
                first_token = int(polish_stack.pop())
                second_token = int(polish_stack.pop())
                curr_sum = str(first_token + second_token)
                polish_stack.append(curr_sum)
            elif token == "-":
                first_token = int(polish_stack.pop())
                second_token = int(polish_stack.pop())
                curr_sum = str(second_token - first_token)
                polish_stack.append(curr_sum)

            elif token == "*":
                first_token = int(polish_stack.pop())
                second_token = int(polish_stack.pop())
                curr_sum = str(second_token * first_token)
                polish_stack.append(curr_sum)
            
            elif token == "/":
                first_token = int(polish_stack.pop())
                second_token = int(polish_stack.pop())
                curr_sum = math.trunc(second_token / first_token)
                polish_stack.append(curr_sum)
            else:
                polish_stack.append(token)
         
        return int(polish_stack[-1])






