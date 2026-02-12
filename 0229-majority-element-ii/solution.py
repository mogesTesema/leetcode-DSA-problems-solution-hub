class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        freq_nums = Counter(nums)
        cut_off = len(nums)//3
        ans = []

        for key, val in freq_nums.items():
            if val > cut_off:
                ans.append(key)
        return ans
        
