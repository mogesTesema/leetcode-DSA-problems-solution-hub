class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for _ in range(numCourses)]
        inDegree = [0]*numCourses
        for course, prerq in prerequisites:
            courses[prerq].append(course)
            inDegree[course] += 1

        taken = set()
        queue = deque()
       
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        # print(queue)
        while queue:
            take = queue.popleft()
            taken.add(take)
            for dep in courses[take]:
                inDegree[dep] -= 1
                if inDegree[dep] == 0:
                    queue.append(dep)
        return len(taken) == numCourses
                

