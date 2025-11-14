class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # set_one = set(nums1)
        # set_two = set(nums2)
        # return list(set_one.intersection(set_two))
        nums1.sort()
        nums2.sort()
        pointer_one = 0
        pointer_two = 0
        answer = []
        while pointer_one < len(nums1) and pointer_two < len(nums2):
            if nums1[pointer_one] == nums2[pointer_two]:
                if nums1[pointer_one] not in answer:
                    answer.append(nums1[pointer_one])
                pointer_one += 1
                pointer_two += 1
                
            elif nums1[pointer_one] < nums2[pointer_two]:
                pointer_one += 1
            else:
                pointer_two += 1
        return answer



