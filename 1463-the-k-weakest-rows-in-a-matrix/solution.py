class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strenght = []
        heapify(strenght)
        for index,row in enumerate(mat):
            heappush(strenght,(row.count(1),index))
        return [index for _ , index in nsmallest(k,strenght)]

        
