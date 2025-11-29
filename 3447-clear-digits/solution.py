class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        nums = [str(num) for num in range(0,10)]
        for char in s:
            if char in nums:
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        ans = "".join(stack)
        return ans
