class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        words = []
        heapify(words)
        for item in freq:
            heappush(words,(-freq[item],item))
        ans = []
        while len(ans) < k:
            ans.append(heappop(words)[1])

        return ans
        


        
