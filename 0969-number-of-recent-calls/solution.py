from collections import deque

class RecentCounter:

    def __init__(self):
        self.counter = deque()  # use deque for efficient pops from the left

    def ping(self, t: int) -> int:
        self.counter.append(t)
        # remove all times older than t - 3000
        while self.counter[0] < t - 3000:
            self.counter.popleft()
        return len(self.counter)


# Example usage:
# obj = RecentCounter()
# print(obj.ping(1))     # 1
# print(obj.ping(100))   # 2
# print(obj.ping(3001))  # 3
# print(obj.ping(3002))  # 3

