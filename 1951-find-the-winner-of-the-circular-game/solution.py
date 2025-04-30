class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(_ for _ in range(1,n+1))
        current= 0
        while(len(friends)!=1):
            current = (current +k -1)%len(friends)
            del friends[current]
        return friends[0]
            


            
        
