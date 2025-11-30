class Solution:
    def firstUniqChar(self, s: str) -> int:
        frq = Counter(s)
        print(frq)
        
        for index,chr in enumerate(s):
            if frq[chr] == 1:
                return index
        return -1
