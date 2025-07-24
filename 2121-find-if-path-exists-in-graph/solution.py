class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        how to approach the problem?
        1.understand the problem
            a. input
            b. output
            c. relation between input and output
        2.explore with concerate example
            a. simple test
            b. edge test
            c. input input
            d. invalid input

        3.break it down
            a. make simplified version without thinking about syntax
                1. change input into adjacency list
                    a. create graph array that will contian each vertix's neighborers vertices.
                    b. iterate through input, add to graph list with bi-direction
                
                2.starting from source node route to destination node using DFS
                    a. create visited list and pathFound variable with False

                    b. recursivly visit node and check for distination
            c. make high level psdocode
            
        4.solve and simplify
        5. refactore
            a. you have solved but not done.
        """
    
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
