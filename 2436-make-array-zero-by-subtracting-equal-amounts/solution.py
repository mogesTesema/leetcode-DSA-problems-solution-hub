class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums)-{0})
        # nums = [x for x in nums if x > 0]
        # heapify(nums)
        # operation = 0
        # while nums:
        #     smallest = heappop(nums)
        #     nums = [x-smallest for x in nums if x - smallest > 0]
        #     heapify(nums)
        #     operation += 1
        # return operation
