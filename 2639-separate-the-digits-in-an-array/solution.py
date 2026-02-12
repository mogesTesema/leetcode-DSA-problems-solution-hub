class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            num = [int(x) for x in str(num)]
            ans.extend(num)
        
        return ans

        
