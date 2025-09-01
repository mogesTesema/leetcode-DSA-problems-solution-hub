class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
       
        inDegree = {i:0 for i in range(n)}
        for source, distination in edges:
            inDegree[distination] += 1
        ans = []
        
        # print("\n", inDegree)
        for index, val in inDegree.items():
            if val == 0:
                ans.append(index)
        return ans

