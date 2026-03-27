class Solution:
    def totalNQueens(self, n: int) -> int:

        cols = set()
        pos_dig = set() # r + c
        neg_dig = set() # r-c
        solution = 0

        def backtrack(r):

            if r == n:
                nonlocal solution
                solution += 1
                return
            
            for col in range(n):
                curr_pos_dig = r + col
                curr_neg_dig = r - col

                if col in cols or curr_pos_dig in pos_dig or curr_neg_dig in neg_dig:
                    continue

                cols.add(col)
                pos_dig.add(curr_pos_dig)
                neg_dig.add(curr_neg_dig)

                backtrack(r+1)

                cols.remove(col)
                pos_dig.remove(curr_pos_dig)
                neg_dig.remove(curr_neg_dig)
        
        backtrack(0)

        return solution
