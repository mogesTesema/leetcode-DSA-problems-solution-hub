import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Add original index to each task and sort by enqueue time
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort()
        
        n = len(tasks)
        task_idx = 0
        current_time = 0
        result = []
        available_tasks = [] # This is the min-heap
        
        while len(result) < n:
            # Add all tasks that have arrived by the current time
            while task_idx < n and tasks[task_idx][0] <= current_time:
                enqueue_time, processing_time, original_index = tasks[task_idx]
                heapq.heappush(available_tasks, (processing_time, original_index))
                task_idx += 1
            
            # If no tasks are available, advance time to the next task's arrival
            if not available_tasks:
                current_time = tasks[task_idx][0]
                continue
            
            # Pop the task with the shortest processing time
            processing_time, original_index = heapq.heappop(available_tasks)
            
            # Update the current time and append the task index to the result
            current_time += processing_time
            result.append(original_index)
            
        return result
