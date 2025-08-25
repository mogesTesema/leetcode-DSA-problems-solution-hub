import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = []
        res = []
        for i in range(len(nums1)):
            heapq.heappush(pq, (nums1[i] + nums2[0], i, 0))
        for _ in range(k):
            s, i, j = heapq.heappop(pq)
            res.append([nums1[i], nums2[j]])
            if j != len(nums2) - 1:
                heapq.heappush(pq, (nums1[i] + nums2[j+1], i, j+1))
        return res


