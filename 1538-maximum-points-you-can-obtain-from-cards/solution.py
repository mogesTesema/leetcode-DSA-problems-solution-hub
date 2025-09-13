class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_points = sum(cardPoints)
        window_size = len(cardPoints)-k
        current_window = sum(cardPoints[:window_size])
        ans = total_points - current_window

        for i in range(window_size,len(cardPoints)):
            current_window -= cardPoints[i-window_size]
            current_window += cardPoints[i]
            ans = max(ans, total_points-current_window)
        return ans

