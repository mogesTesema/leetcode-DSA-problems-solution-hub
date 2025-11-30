class RecentCounter:

    def __init__(self):
        self.timer = deque()
        

    def ping(self, t: int) -> int:
        min_time = t - 3000
        self.timer.append(t)
        while self.timer and self.timer[0] < min_time:
            self.timer.popleft()
        return len(self.timer)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
