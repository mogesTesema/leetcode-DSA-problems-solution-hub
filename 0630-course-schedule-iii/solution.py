class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # course_heap = []
        # heapify(course_heap)
        # for duration, lastDay in courses:
        #     heappush(course_heap, (lastDay,duration))
        # # print(course_heap)
        # course_finished = 0
        # totalDays = 0
        # while course_heap:
        #     deadline, duration = heappop(course_heap)
        #     if deadline >= duration + totalDays:
        #         course_finished += 1
        #         totalDays += duration
        # return course_finished
 # Step 1: sort by deadline
        courses.sort(key=lambda x: x[1])

        totalDays = 0
        max_heap = []  # store durations as negative for max-heap behavior

        for duration, lastDay in courses:
            if totalDays + duration <= lastDay:
                # take course
                heapq.heappush(max_heap, -duration)
                totalDays += duration
            elif max_heap and -max_heap[0] > duration:
                # replace the longest course with this shorter one
                totalDays += duration + heapq.heappop(max_heap)
                heapq.heappush(max_heap, -duration)

        return len(max_heap)

        
