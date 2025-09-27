from itertools import combinations

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(A, B, C):
            return abs(
                A[0]*(B[1]-C[1]) + 
                B[0]*(C[1]-A[1]) + 
                C[0]*(A[1]-B[1])
            ) / 2
        
        max_area = 0
        # print(combinations(points,3))
        for A, B, C in combinations(points, 3):
            max_area = max(max_area, area(A, B, C))
        return max_area

