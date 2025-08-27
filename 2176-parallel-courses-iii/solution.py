class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj_lst = defaultdict(list)
        # creating and storing neighbors via adjacency list
        for s, d in relations:
            adj_lst[s].append(d)
        
        visited = set()
        def traverse(x):
            if x in visited:
                # if x node has already finished visiting all its neighbors and updated its 
                # max time, we can just return the max time for it
                return time[x-1]
            tt = 0
            for nei in adj_lst[x]:
                tt = max(tt, traverse(nei))
            # since we have visited all its neighbors we add to visited set
            visited.add(x)
            # update the time it takes from the given node as sum 
            # of its own time plus the maximum time from its neighbors
            time[x-1] += tt
            return time[x-1]
        
        for j in range(1, n+1):
            if j not in visited:
                traverse(j)
        return max(time)
