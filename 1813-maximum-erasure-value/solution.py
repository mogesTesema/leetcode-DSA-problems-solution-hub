class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = 0
        current_sum = 0
        max_sum = 0
        
        for right, x in enumerate(nums):
            # Shrink window if duplicate
            while x in seen:
                # Remove nums[left] from window
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1
                
            # Add the new one
            seen.add(x)
            current_sum += x
            
            # Update max
            if current_sum > max_sum:
                max_sum = current_sum
                
        return max_sum

