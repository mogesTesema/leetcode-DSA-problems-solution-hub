class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        counted = 0
        """
        how to solve the problem?
            1. understand the problem
                .a express in you way: counting hills and vallys in array road.
            2. explore with concrate example
            3. break it down
                . check for hill and vally for each numbers if their is the same number, find next number
            4. solve/simplify
            5. refactor
        """
        i = 1
        j = 0
        while (i < len(nums)):
            j = i + 1
            while j < len(nums) and (nums[j]== nums[i]):
                j += 1
            if j == len(nums):
                break
            if nums[i-1] < nums[i] > nums[j]:
                counted += 1
            elif nums[i-1] > nums[i] <nums[j]:
                counted += 1
            i = j
        return counted

            

