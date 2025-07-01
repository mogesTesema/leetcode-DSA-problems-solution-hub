class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        result = []
        
        dRow = [0, 1, 0, -1]
        dCol = [1, 0, -1, 0]
        
        direction = 0
        steps = 1
        
        r, c = rStart, cStart
        
        result.append([r, c])
        
        totalCells = rows * cols
        
        while len(result) < totalCells:
            for _ in range(steps):
                r += dRow[direction]
                c += dCol[direction]
                
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
                    
            direction = (direction + 1) % 4
            
            if direction % 2 == 0: 
                steps += 1
                
        return result
