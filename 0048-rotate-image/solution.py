class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)-1
        old = copy.deepcopy(matrix)
        for i in range(n+1):
            for j in range(len(matrix[0])):
                matrix[j][n-i] = old[i][j]
        # pattern of rotated and orginal matrix, in new rotated matrix: i = j and j = n-i
        

