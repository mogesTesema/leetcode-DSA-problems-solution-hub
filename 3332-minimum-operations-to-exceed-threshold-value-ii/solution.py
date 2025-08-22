class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        min_operation = 0
        length = len(nums)
        smallest = None
        second_smallest = None
        if length >= 2:
            smallest = heappop(nums)
            heappush(nums, smallest)
        while smallest < k and length >= 2:
            min_operation += 1
            smallest = heappop(nums)
            second_smallest = heappop(nums)
            heappush(nums, min(smallest,second_smallest)*2 + max(smallest,second_smallest))
            smallest = heappop(nums)
            heappush(nums, smallest)
            length = len(nums)
            
        return min_operation
