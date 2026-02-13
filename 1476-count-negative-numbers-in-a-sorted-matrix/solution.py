class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        rows,cols = len(grid),len(grid[0])
        count = 0


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] < 0:
                    count += 1 
        
        return count


        
