class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [ -1*x for x in gifts]
        heapify(gifts)
        # print(gifts)
        while k:
            k -= 1
            val = -1*heappop(gifts)
            val = floor(sqrt(val))
            heappush(gifts,-1*val)
        return -1*sum(gifts)
        
