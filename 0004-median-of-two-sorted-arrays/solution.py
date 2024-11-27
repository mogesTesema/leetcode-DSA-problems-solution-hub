class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        l=len(nums1)
        if l%2==0:
            l=l//2
            return (nums1[l-1]+nums1[l])/2
        else:
            l=l//2
            return float(nums1[l])
