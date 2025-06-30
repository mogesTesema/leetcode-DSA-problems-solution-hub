class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums = [i for i in range(0, int(sqrt(c))+1)]
        left = 0
        right = len(nums)-1
        while left <= right:
            # if nums[left]*nums[left] == c and nums[right]*nums[right] == c:
            #     return True 
            sum = nums[left]*nums[left] + nums[right]*nums[right]
            if sum == c:
                return True
            if sum > c:
                right -= 1
            else:
                left += 1
        return False




        
