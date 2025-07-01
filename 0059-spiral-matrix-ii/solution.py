class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        
        num = 1
        rowBegin = 0
        rowEnd = n - 1
        colBegin = 0
        colEnd = n - 1

        while rowBegin <= rowEnd and colBegin <= colEnd:
            # Traverse Right
            for j in range(colBegin, colEnd + 1):
                matrix[rowBegin][j] = num
                num += 1
            rowBegin += 1

            # Traverse Down
            for i in range(rowBegin, rowEnd + 1):
                matrix[i][colEnd] = num
                num += 1
            colEnd -= 1

            # Traverse Left
            if rowBegin <= rowEnd:
                for j in range(colEnd, colBegin - 1, -1):
                    matrix[rowEnd][j] = num
                    num += 1
                rowEnd -= 1

            # Traverse Up
            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin - 1, -1):
                    matrix[i][colBegin] = num
                    num += 1
                colBegin += 1
        
        return matrix
