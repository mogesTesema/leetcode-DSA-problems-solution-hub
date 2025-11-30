class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        bob = 0
        alice = len(piles)
        total = 0

        while bob < alice:
            bob += 1
            alice -= 2
            total += piles[alice]
        return total



