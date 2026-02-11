class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_one = set(nums1)
        set_two = set(nums2)
        uniqe_one = set_one - set_two
        uniqe_two = set_two - set_one

        return [list(uniqe_one),list(uniqe_two)]
