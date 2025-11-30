class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        from collections import deque
        
        players = deque(range(1, n + 1))
        
        while len(players) > 1:
            step = (k - 1) % len(players)
            for _ in range(step):
                players.append(players.popleft())
            players.popleft()  
        
        return players[0]

