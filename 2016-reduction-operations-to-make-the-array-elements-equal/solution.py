class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        operations = 0
        for i in range(1,n):
            if nums[i-1] != nums[i]:
                operations += i
        return operations
        
