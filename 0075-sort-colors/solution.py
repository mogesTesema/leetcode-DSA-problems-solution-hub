class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        frq = defaultdict()
        for num in nums:
            frq[num] = frq.get(num,0) + 1
        
        nums_two = []
        if 0 in frq:
            nums_two.extend([0]*frq[0])
        if 1 in frq:
            nums_two.extend([1]*frq[1])
        if 2 in frq:
            nums_two.extend([2]*frq[2])
        for index,num in enumerate(nums_two):
            nums[index] = num
            
        print(nums)
