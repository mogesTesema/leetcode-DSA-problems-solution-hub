

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min_heap = nums[:k]
        # heapify(min_heap)
        # for num in nums[k:]:
        #     if num > min_heap[0]:
        #         heappop(min_heap)
        #         heappush(min_heap,num)
        # return min_heap[0]
        """
        secondary solution: gather k larger num and then return smallest of those larger numbers
        """
        heapify(nums)
        return nlargest(k,nums)[-1]


