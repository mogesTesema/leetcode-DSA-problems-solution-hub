class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
            # nums[:] = [i for i in nums if i != val]
            # return len(nums)
            left = 0 
            right = len(nums) - 1
            while left <= right:
                if nums[right] == val:
                    nums[right] = "_"
                    right -= 1
                elif nums[left] == val:
                    nums[left],nums[right] = nums[right],"_"
                    left += 1
                    right -= 1
                else:
                    left += 1
            counter = 0
            for num in nums:
                if num == "_":
                    return counter
                else:
                    counter += 1
            return counter


