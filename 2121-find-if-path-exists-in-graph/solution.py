class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    
    
        # sub solution one
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
