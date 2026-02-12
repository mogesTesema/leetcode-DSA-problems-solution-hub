class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        nums = list(num_set)
        nums.sort()
        print(nums)

        left = 0 
        right = 0
        max_len = 0

        while right < len(nums):

            while right < len(nums)-1 and nums[right]+1 == nums[right+1]:
                right += 1
           
            right += 1
            max_len = max(max_len, right -left)
            left = right
            
        
        return max_len
            


