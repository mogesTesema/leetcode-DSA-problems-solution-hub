class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # heap approach
        nums = [-x for x in nums]
        heapify(nums)
        num1 = -1*heappop(nums)
        num2 = -1*heappop(nums)
        return (num1-1)*(num2-1)
        '''
        #naive solution:

        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)
        '''
        
