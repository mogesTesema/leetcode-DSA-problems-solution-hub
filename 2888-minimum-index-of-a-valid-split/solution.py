from collections import Counter

class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        n = len(nums)
        total_count = Counter(nums)
        dominant, _ = total_count.most_common(1)[0]

        left_count = 0
        for i in range(n - 1):
            if nums[i] == dominant:
                left_count += 1
            if left_count > (i + 1) // 2 and total_count[dominant] - left_count > (n - i - 1) // 2:
                return i
        return -1
