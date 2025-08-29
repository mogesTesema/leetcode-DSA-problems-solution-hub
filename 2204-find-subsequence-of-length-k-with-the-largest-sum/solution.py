class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums = [(-x, i) for i, x in enumerate(nums)]
        heapify(nums)
        ans = nsmallest(k, nums)
        ans = sorted(ans, key=lambda x: x[1])
        ans = [-1*item[0] for item in ans]
        return ans

        
        
