class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for row in matrix:
            larger = max(row)
            smaller = min(row)
            if len(set(row)) < len(row):
                return False
            if larger > len(row) or smaller < 1:
                return False
        for i in range(len(matrix[0])):
            colum = []
            for j in range(len(matrix)):
                colum.append(matrix[j][i])
            larger = max(colum)
            smaller = min(colum)
            if len(set(colum)) < len(colum):
                return False
            if larger > len(colum) or smaller < 1:
                return False
        return True
                


        
