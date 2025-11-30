class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        path_stack = []
        for cmd in path:
            print(cmd)
            if cmd == "" or cmd == ".":
                continue
            if cmd == "..":
                if path_stack:
                    path_stack.pop()
            else:
                path_stack.append(cmd)
        absolute_path = "/"
        absolute_path += "/".join(path for path in path_stack)
        
        return absolute_path
