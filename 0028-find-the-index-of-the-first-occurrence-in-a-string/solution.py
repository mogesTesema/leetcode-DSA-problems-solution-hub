class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # if needle in haystack:
        #     haystack = haystack.split(needle)
        #     return len(haystack[0])
        # else:
        #     return -1
        i = 0
        while i < len(haystack):
            j = 0 
            starting = i
            while j < len(needle) and i<len(haystack) and needle[j] == haystack[i]:
                i += 1
                j += 1
         
            if j == len(needle):
                return starting
            i = starting + 1

        return -1
        
        
