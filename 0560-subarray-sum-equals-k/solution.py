class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = {0: 1}
        res = 0
        sum = 0
        for num in nums:
            sum += num
            if (sum - k) in map:
                res += map[sum - k]

            map[sum] = map.get(sum, 0) + 1

        return res
