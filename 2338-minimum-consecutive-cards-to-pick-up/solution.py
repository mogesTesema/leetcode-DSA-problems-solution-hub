class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_seen = {}
        min_len = float('inf')
        
        for i, card in enumerate(cards):
            if card in last_seen:
                min_len = min(min_len, i - last_seen[card] + 1)
            last_seen[card] = i
        
        return -1 if min_len == float('inf') else min_len

