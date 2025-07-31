class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        for key, value in prerequisites:
            courses[key].append(value)

        visited = set()
        cycle = set()


        def dfs(c):
            if c in cycle:
                return False
            if c in visited:
                return True
            if not courses[c]:
                return True
            
            cycle.add(c)
            for pre in courses[c]:
                if not dfs(pre):
                    return False
            cycle.remove(c)
            visited.add(c)
            return True
                

        for course in prerequisites:
            if not dfs(course[1]):
                return False
        return True
