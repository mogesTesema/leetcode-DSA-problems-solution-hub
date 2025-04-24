class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        current = 0
        minLen = float('inf')
        while(right<len(nums)):
           current += nums[right]
           right +=1
           while(current>=target):
            minLen = min(minLen, right-left)
            current -= nums[left]
            left +=1

        return minLen if minLen != float('inf') else 0


        
