class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elem = []
        for index,num in enumerate(nums):
            elem.append([num,index])
        
        elem.sort()
       
        left = 0
        right = len(elem)-1
        ans = []
        while left < right:
          
            curr_sum = elem[left][0] + elem[right][0]

            if curr_sum == target:
                ans.append(elem[left][1])
                ans.append(elem[right][1])
                return ans
            if curr_sum > target:
                right -= 1
            else:
                left += 1

