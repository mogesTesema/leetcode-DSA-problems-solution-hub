class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        roots = {i:i for i in range(n)}
        def find(i):
            return i if i == roots[i] else find(roots[i])
        def union(i,j):
            r1, r2 = find(i), find(j)
            if r1 != r2:
                roots[r2] = r1
        def get_components():
            d = {}
            for k, v in roots.items():
                root = find(v)
                if root not in d:
                    d[root] = {k}
                else:
                    d[root].add(k)
            return len(d)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    union(i,j)
        return get_components()

