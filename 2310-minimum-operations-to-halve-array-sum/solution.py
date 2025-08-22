class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        half = total/2
        k = 0
        nums = [-1*x for x in nums]
        heapify(nums)
        print(total,half,nums)
        while total > half:
            k += 1
            val = -1*heappop(nums)
            val = val/2
            total -= val
            heappush(nums,-1*val)
        return k
        
