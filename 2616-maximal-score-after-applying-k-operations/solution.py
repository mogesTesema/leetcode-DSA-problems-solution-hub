class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        starting_score = 0
        nums = [-1*k for k in nums]
        heapify(nums)
        while k:
            k -= 1
            val = -1*heappop(nums)
            starting_score += val
            val = -1*ceil(val/3)
            heappush(nums,val)
        return starting_score
