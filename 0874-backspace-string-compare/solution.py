class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        editor_s = []
        editor_t = []
        for char in s:
            if editor_s and char == "#":
                editor_s.pop()
            if char != "#":
                editor_s.append(char)
        for char in t:
            if editor_t and char == "#":
                editor_t.pop()
            if char != "#":
                editor_t.append(char)
                
        return editor_s == editor_t

        
