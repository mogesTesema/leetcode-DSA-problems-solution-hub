class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = defaultdict(int)
        for color in nums:
            colors[color] = colors.get(color,0) +1
        print(colors)
        nums[:] = []
        for i in range(3):
            nums.extend([i]*colors[i])
        print(nums)
