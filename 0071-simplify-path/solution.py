class Solution:
    def simplifyPath(self, path: str) -> str:

        path = [p for p in path.split('/') if p!=""]
        
        stack = []
       

        for p in path:
            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            elif p == ".":
                continue
            else:
                stack.append(p)
        
        return "/" + "/".join(stack)
