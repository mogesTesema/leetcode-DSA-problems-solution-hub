class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = len(nums)/3
        counted_elem = Counter(nums)
        ans = []
        for key in counted_elem:
            if counted_elem[key] > freq:
                ans.append(key)
        return ans
