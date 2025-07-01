class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        if not matrix:
            return res

        rowBegin = 0
        rowEnd = len(matrix) - 1
        colBegin = 0
        colEnd = len(matrix[0]) - 1

        while rowBegin <= rowEnd and colBegin <= colEnd:
            # Traverse Right
            for j in range(colBegin, colEnd + 1):
                res.append(matrix[rowBegin][j])
            rowBegin += 1

            # Traverse Down
            for i in range(rowBegin, rowEnd + 1):
                res.append(matrix[i][colEnd])
            colEnd -= 1

            # Traverse Left
            if rowBegin <= rowEnd:  # Check if there's a row to traverse
                for j in range(colEnd, colBegin - 1, -1):
                    res.append(matrix[rowEnd][j])
                rowEnd -= 1

            # Traverse Up
            if colBegin <= colEnd:  # Check if there's a column to traverse
                for i in range(rowEnd, rowBegin - 1, -1):
                    res.append(matrix[i][colBegin])
                colBegin += 1

        return res
