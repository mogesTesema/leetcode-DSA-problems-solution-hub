class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        rep = [i for i in range(n)]
        size = [1]*n
        def find(x):
            """
            iterative approach
            """
            # while x != rep[x]:
            #     rep[x] = rep[rep[x]]
            #     x = rep[x]
            # return rep[x]
            return x if x == rep[x] else find(rep[x])
        def union(x,y):
            rootx, rooty = find(x), find(y)
            if rootx != rooty:
                if size[rootx] > size[rooty]:
                    rep[rooty] = rootx
                    size[rootx] += size[rooty]
                else:
                    rep[rootx] = rooty
                    size[rooty] += size[rootx]
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]==1:
                    union(i,j)
        counter = 0
        for first_rep, current_rep in enumerate(rep):
            if first_rep == current_rep:
                counter += 1
        return counter

