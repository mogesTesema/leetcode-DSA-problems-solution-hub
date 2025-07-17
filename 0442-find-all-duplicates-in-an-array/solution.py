class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # sorth elements using cyclic sort and then check occurance of element
        duplicated = []
        # n = len(nums)
        # i = 0
        # current_position = 0
        # while i < n:
        #     current_position = nums[i] -1
        #     if current_position != i:
        #         nums[current_position], nums[i] = nums[i], nums[current_position]
        #     else:
        #         i += 1
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                duplicated.append(nums[i])
        return duplicated
                
        
