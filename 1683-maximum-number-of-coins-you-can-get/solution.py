class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        left = 0
        right = len(piles) -1
        piles.sort()

        my_piles = 0

        while left < right:
            my_piles += piles[right-1]
            right -= 2
            left += 1

        return my_piles
        
