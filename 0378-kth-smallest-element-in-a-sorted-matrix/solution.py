class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flat_list = []
        for llist in matrix : 
            flat_list.extend(llist)

        flat_list.sort()

        return flat_list[k-1]
