class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        for row in grid:
            row.sort(reverse=True)
            

        # print(grid)
        ans = 0
        larger = []
        heapify(larger)
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                heappush(larger, -1*grid[j][i])
            ans += -1*heappop(larger)
            larger = []
            heapify(larger)
        return ans



