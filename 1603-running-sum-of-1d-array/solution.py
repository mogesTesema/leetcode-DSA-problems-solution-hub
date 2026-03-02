class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        

        if len(nums) == 0:
            return []

        prev = nums[0]

        for i in range(1,len(nums)):
            nums[i] = nums[i] + prev
            prev = nums[i]

        return nums


        
