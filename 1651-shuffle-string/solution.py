class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
         empty_str = [""]*len(s)
         s = list(s)
         for str_idx,index in enumerate(indices):
            empty_str[index] = s[str_idx]
         return "".join(empty_str)
        
