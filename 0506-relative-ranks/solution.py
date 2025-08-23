import heapq

class Solution:
    def findRelativeRanks(self, score):
        res = [""] * len(score)
        index_map = {s: i for i, s in enumerate(score)}  # same as HashMap in Java

        # maxHeap using negative values because Python's heapq is min-heap by default
        max_heap = [-s for s in score]
        heapq.heapify(max_heap)

        rank = 1
        while max_heap:
            current_score = -heapq.heappop(max_heap)  # negate to get original score
            index = index_map[current_score]

            if rank == 1:
                res[index] = "Gold Medal"
            elif rank == 2:
                res[index] = "Silver Medal"
            elif rank == 3:
                res[index] = "Bronze Medal"
            else:
                res[index] = str(rank)

            rank += 1

        return res

