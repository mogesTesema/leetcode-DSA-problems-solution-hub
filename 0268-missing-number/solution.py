class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       original_set = set(range(0,len(nums)+1))
       x = original_set - set(nums)
       for num in x:
        return num

        
