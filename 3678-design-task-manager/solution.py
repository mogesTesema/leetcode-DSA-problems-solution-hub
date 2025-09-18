import heapq

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self._d = {
            taskId: (userId, priority)
            for userId, taskId, priority in tasks
        }
        self._h = [
            (-priority, -taskId, userId)
            for userId, taskId, priority in tasks
        ]
        heapq.heapify(self._h)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self._d[taskId] = (userId, priority)
        heapq.heappush(self._h, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, priority = self._d[taskId]
        if newPriority != priority:
            self._d[taskId] = (userId, newPriority)
            heapq.heappush(self._h, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        self._d.pop(taskId)

    def execTop(self) -> int:
        while self._h:
            priority, taskId, userId = heapq.heappop(self._h)
            taskId *= -1
            if self._d.get(taskId, (None, None)) == (userId, -priority):
                self._d.pop(taskId)
                return userId
        return -1
