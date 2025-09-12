class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_w = float('inf')
        min_w = blocks[:k].count("W")
        print(min_w)
        current_w = min_w
        for i in  range(k,len(blocks)):
            if blocks[i] =="W":
                current_w +=1
            if blocks[i-k] == "W":
                current_w -= 1
            min_w = min(current_w,min_w)
        return min_w
        
