class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        freq_nums = Counter(nums)

        for num in freq_nums:
        
            if freq_nums[num] == 1:
                
                return num
        
