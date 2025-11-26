class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        for i, x in enumerate(nums):
            if prefix == total - prefix - x:
                return i
            prefix += x
        return -1

