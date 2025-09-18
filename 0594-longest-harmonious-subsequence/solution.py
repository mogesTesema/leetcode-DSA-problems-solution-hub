class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        c = Counter(nums)
        numset = set(nums)

        for num in numset:
            if num+1 in c:
                ans = max(ans,c[num]+c[num+1])

        return ans
