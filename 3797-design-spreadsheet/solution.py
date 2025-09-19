class Spreadsheet:
    """
    how to tackle this problem?
    1. create 2D with defualt 0 valued tensor to store value
    2. map A-Z letter into 0-25 matrix index
    3. check if the computation is a number or cell via slicing and then check if the sign found in the given dictionary

    """

    def __init__(self, rows: int):
        self.index_map = {letter: index for index, letter in enumerate(string.ascii_uppercase)}
        self.matrix = [[0]*26 for i in range(rows)]
        

    def setCell(self, cell: str, value: int) -> None:
        colum = cell[0]
        colum = self.index_map[colum]
        row = int(cell[1:]) - 1 # reduce row by one to make it 0-indexed array: e.g row 25 in 1-indexed become row 24 in 0-indexed array
        self.matrix[row][colum] = value
        

    def resetCell(self, cell: str) -> None:
        colum = cell[0]
        colum = self.index_map[colum]
        row = int(cell[1:]) - 1
        self.matrix[row][colum] = 0
        

    def getValue(self, formula: str) -> int:
        formula = formula.split("+")
        x = formula[1]
        y = formula[0][1:]
        if x[0] in self.index_map:
            colum_x = self.index_map[x[0]]
            row_x = int(x[1:]) - 1
            x = self.matrix[row_x][colum_x]

        else:
            x = int(x)
        if y[0] in self.index_map:
            colum_y = self.index_map[y[0]]
            row_y = int(y[1:]) - 1
            y = self.matrix[row_y][colum_y]
        else:
            y = int(y)
        return x + y
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
