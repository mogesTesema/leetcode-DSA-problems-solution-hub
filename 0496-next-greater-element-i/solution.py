class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {num:index for index, num in enumerate(nums1)}
        ans = [-1]*len(nums1)
        stack = []
        for index,num in enumerate(nums2):
            
            while stack and stack[-1] < num:
                look = stack.pop()
                ans[nums1_dict[look]] = num
            if num in nums1:
                stack.append(num)
        return ans




