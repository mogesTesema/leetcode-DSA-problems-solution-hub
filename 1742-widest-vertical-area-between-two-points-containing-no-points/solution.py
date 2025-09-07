class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_list = [i[0] for i in points]
        x = sorted(x_list)
        diff = []
        for i in range(1, len(x)):
            diff.append(x[i] - x[i-1])
        return max(diff)
