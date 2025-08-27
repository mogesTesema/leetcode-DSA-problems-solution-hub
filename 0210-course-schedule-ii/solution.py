from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [set() for i in range(numCourses)]
        for relation in prerequisites:
            graph[relation[0]].add(relation[1])  # course -> prereqs list


        inDegree = [0]*numCourses
        for node in range(numCourses):
            for neigh in graph[node]:
                inDegree[neigh] += 1
        queue = deque()
        for course in range(numCourses):
            if inDegree[course] == 0:
                queue.append(course)

        ans = []
        while queue:
            take = queue.popleft()
            ans.append(take)

            for neigh in graph[take]:
                inDegree[neigh] -= 1
                if inDegree[neigh] == 0:
                    queue.append(neigh)
            # for course in graph:
            #     if take in graph[course]:
            #         graph[course].remove(take)   
            #         if len(graph[course]) == 0:
            #             queue.append(course)

        return ans[::-1] if len(ans) == numCourses else []

