class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
    
      
        k %= len(nums)

        nums.reverse()
    
        nums[:k] = reversed(nums[:k])
    
        nums[k:] = reversed(nums[k:])

        """
        Do not return anything, modify nums in-place instead.
        """
        
