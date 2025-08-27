class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount = [-x for x in amount if x > 0]
        heapify(amount)
        second = 0
        while amount:
            cup1 = -heappop(amount)
            cup2 = 0
            if len(amount) >= 1:
                cup2 = -heappop(amount)
                if cup2-1 > 0:
                    heappush(amount,-1*(cup2-1))
            if cup1-1 > 0:
                heappush(amount,-1*(cup1-1))
            second += 1
        return second
            

        
