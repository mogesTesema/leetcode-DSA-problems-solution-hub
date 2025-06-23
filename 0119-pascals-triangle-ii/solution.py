class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        rows = [[1],[1,1]]
        for i in range(2,rowIndex+1):
            rows.append([0]*(i+1))
            rows[i][0] = 1
            rows[i][-1] = 1
            for j in range(1,i):
                rows[i][j] = rows[i-1][j-1] + rows[i-1][j]
        return rows[rowIndex]
        
