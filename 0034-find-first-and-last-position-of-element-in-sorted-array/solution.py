class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                left = mid-1
                right = mid + 1
                while left >= 0 and nums[left] == nums[mid]:
                    left -= 1
                while right < len(nums) and nums[right] == nums[mid]:
                    right += 1
                return [left +1, right -1]
    
        return [-1, -1]
        
