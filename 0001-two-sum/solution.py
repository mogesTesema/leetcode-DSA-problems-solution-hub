class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        left = 0 
        right = len(nums) -1

        sorted_nums = [[val,index] for index, val in enumerate(nums)]
        sorted_nums.sort()
        while left < right:
            curr_sum = sorted_nums[left][0] + sorted_nums[right][0]

            if curr_sum == target:
                return [sorted_nums[left][1],sorted_nums[right][1]]
            if curr_sum < target:
                left += 1
            else:
                right -= 1

        
