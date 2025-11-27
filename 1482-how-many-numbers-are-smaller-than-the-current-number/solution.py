class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_copy = nums[:]
        nums.sort()
        for index in range(len(nums)):
            nums_copy[index] = nums.index(nums_copy[index])
        return nums_copy
