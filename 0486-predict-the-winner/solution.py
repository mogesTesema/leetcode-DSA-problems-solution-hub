class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        
        n = len(nums)

        def score(left,right):
            if left > right:
                return 0

            take_left = nums[left] - score(left+1,right)
            take_right = nums[right] - score(left,right-1)

            return max(take_left,take_right)

        return score(0,n-1) >= 0
