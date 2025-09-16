class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        def even_odd(a,b):
            return a % 2 != b %2
        left = 0
        right = 0
        longest = 0
        while right < len(nums):
            if nums[right] % 2 == 0 and nums[right] <= threshold:
                left = right
                right += 1
                while right < len(nums) and even_odd(nums[right],nums[right-1]):
                    if nums[right] > threshold:
                        print(right, left)
                        # left = right = right + 1
                        break
            
                    right +=1
                longest = max(longest,right -left)
            elif nums[right] > threshold:
                        left = right = right + 1
            else:
                left = right = right + 1
        return longest

                

