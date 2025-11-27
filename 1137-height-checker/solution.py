class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_copy = heights[:]
        heights.sort()
        counter = 0
        for index in range(len(heights)):
            if heights[index] != heights_copy[index]:
                counter += 1
        return counter

