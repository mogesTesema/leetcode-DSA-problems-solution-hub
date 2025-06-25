class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) -1
        first = -1
        last = -1
        if target not in nums:
            return [first,last]
        while low <= high:
            mid = (low + high)//2
            if nums[mid] < target:
                low = mid + 1
            else:
                first = mid
                high = mid - 1
        low = 0 
        high = len(nums) - 1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] > target:
                high = mid - 1
            else:
                last = mid
                low = mid + 1
        return [first,last]


        # left = 0
        # right = len(nums) - 1
        # while left <= right:
        #     mid = (left + right) // 2
            
        #     if nums[mid] > target:
        #         right = mid - 1
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         left = mid-1
        #         right = mid + 1
        #         while left >= 0 and nums[left] == nums[mid]:
        #             left -= 1
        #         while right < len(nums) and nums[right] == nums[mid]:
        #             right += 1
        #         return [left +1, right -1]
    
        # return [-1, -1]
        
