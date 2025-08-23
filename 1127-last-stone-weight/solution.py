class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*x for x in stones]
        heapify(stones)
        while len(stones) >= 2:
            y = -1*heappop(stones)
            x = -1*heappop(stones)
            if y > x:
                heappush(stones, -1*(y-x))
        if len(stones) == 1:
            return -1*stones[0]
        else:
            return 0


        
