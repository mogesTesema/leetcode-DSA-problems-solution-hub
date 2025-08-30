class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapify(nums)
        ans = []
        while nums:
            alice = heappop(nums)
            bob = heappop(nums)
            ans.append(bob)
            ans.append(alice)
        return ans
        
