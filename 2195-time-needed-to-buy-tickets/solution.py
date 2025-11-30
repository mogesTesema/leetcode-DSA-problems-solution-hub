class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque({index:ticket} for index,ticket in enumerate(tickets))
        counter = 0
        while True:
            front = queue.popleft()
            counter += 1

            for idx in front:
                front[idx] -= 1
                if front[idx] == 0 and idx == k:
                    return counter 
                if front[idx] != 0:
                    queue.append(front)

            
        
