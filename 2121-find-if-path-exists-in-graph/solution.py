class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    
        """
        # naive graph traversal solution
        graph = defaultdict(list)
        for v,u in edges:
            graph[v].append(u)
            graph[u].append(v)
        # sub solution two
        visitedVertex = set()
        def DFS(vertex):

            if vertex == destination:
                return True
            if vertex in visitedVertex:
                return False
            visitedVertex.add(vertex)
            for neighbor in graph[vertex]:
                    if DFS(neighbor):
                        return True
            return False

        return DFS(source)
        """
        # union-find version of problem solution
        roots = [i for i in range(n)]
        rank = [1]*n
        def find(i):
            if i == roots[i]: return i
            roots[i] = find(roots[i])
            return roots[i]

        def union(i,j):
            r1, r2 = find(i), find(j)
            if r1 == r2: return
            if rank[r1] > rank[r2]:
                roots[r2] = r1
            elif rank[r1] < rank[r2]:
                roots[r1] = r2
            else:
                roots[r1] = r2
                rank[r2] += 1
                
        for root1, root2 in edges:
            union(root1,root2)
        return find(source) == find(destination)
