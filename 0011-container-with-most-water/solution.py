class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) -1 
        max_water = 0


        while left < right:
            smaller_height = min(height[left],height[right])
            max_water = max(max_water,(right-left)*smaller_height)
            if smaller_height == height[left]:
                left += 1
            elif smaller_height == height[right]:
                right -= 1

        return max_water
