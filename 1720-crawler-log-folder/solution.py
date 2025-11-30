class Solution:
    def minOperations(self, logs: List[str]) -> int:
        dir_stack = []
        for log in logs:
            if log == "../":
                if dir_stack:
                    dir_stack.pop()
            elif log == "./":
                pass
            else:
                dir_stack.append(log)
        return len(dir_stack)
