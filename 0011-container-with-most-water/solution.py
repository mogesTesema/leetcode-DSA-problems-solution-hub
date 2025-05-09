class Solution:
    def maxArea(self, height: List[int]) -> int:
        left =0
        right = len(height) -1
        maxWater = 0
        lenght = right -left
        width =0
        while left < right:
            lenght = right -left
            width = min(height[left], height[right])
            if width == height[left]:
                left += 1
            else:
                right -= 1
            maxWater = max(maxWater, width * lenght)
        return maxWater



        
