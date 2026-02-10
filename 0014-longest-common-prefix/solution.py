class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        lengths = [len(x) for x in strs]
        min_length = min(lengths)
        prefix = ""
        for i in range(min_length):
            current_char = strs[0][i]
            for chars in strs:
                if chars[i] == current_char:
                    ans += chars[i]
                else:
                    return prefix

            prefix += current_char
        return prefix



        
