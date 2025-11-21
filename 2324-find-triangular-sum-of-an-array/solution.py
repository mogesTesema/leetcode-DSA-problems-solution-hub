class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        length = 0
        while length < len(nums):
            for i in range(0,len(nums)-length-1):
                nums[i] = (nums[i] + nums[i+1]) % 10
            length += 1
        return nums[0]
