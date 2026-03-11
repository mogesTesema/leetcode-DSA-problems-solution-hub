class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ans = [-1]*len(nums1)

        stack = []

        for index,num in enumerate(nums2):

            while stack and stack[-1] < num:
                val = stack.pop()
                if val in nums1:
                    ans[nums1.index(val)] = num
            stack.append(num)

        return ans
            
        
