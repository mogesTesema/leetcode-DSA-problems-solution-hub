class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        rows, cols = len(mat), len(mat[0])
        res = []
        
        for d in range(rows + cols - 1):
            intermediate = []
            
            r = 0 if d < cols else d - cols + 1
            c = d if d < cols else cols - 1
            
            while r < rows and c >= 0:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1
            
            if d % 2 == 0:
                res.extend(intermediate[::-1])
            else:
                res.extend(intermediate)
        
        return res

