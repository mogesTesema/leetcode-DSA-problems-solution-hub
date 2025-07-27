class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        longest = 0
        ans = 0
        for index, value in graph.items():
            if longest < len(value):
                ans = index
                longest = len(value)
        return ans
        
