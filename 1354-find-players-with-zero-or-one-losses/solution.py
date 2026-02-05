class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        winners = set()
        losers = dict()
        for match in matches:
            players.update(match)
            winners.add(match[0])
            losers[match[1]] = losers.get(match[1],0) + 1

        ans = []
        final_losers = [lose for lose in losers if losers[lose] == 1]
       
        final_winners = list(winners - set(losers.keys()))
        final_winners.sort()
        final_losers.sort()
        ans.append(final_winners)
        ans.append(final_losers)
        return ans
     
        
        
