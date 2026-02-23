class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        holder = 0
        seeker = 0

        while seeker < len(nums):
            if nums[holder] == 0 and nums[seeker] != 0:
                nums[holder], nums[seeker] =  nums[seeker], nums[holder]
                holder += 1
                seeker += 1
            elif nums[seeker] == 0:
                seeker += 1

            elif nums[holder] != 0 and nums[seeker] != 0:
                holder += 1
                seeker += 1


