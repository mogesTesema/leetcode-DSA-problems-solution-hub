class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        """
        heap approach solution
        """
        nums = [(x, i) for i, x in enumerate(nums)]
        heapify(nums)
        for _ in range(k):
            num, index = heappop(nums)
            num *= multiplier
            heappush(nums,(num,index))
        nums = sorted(nums, key=lambda x: x[1])
        nums = [num[0] for num in nums]
        return nums
        """
        naive solution
        """
        while k > 0:
            x = min(nums)
            nums[nums.index(x)] = x * multiplier
            k -= 1
        return nums

