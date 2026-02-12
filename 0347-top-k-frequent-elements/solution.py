from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_elem = Counter(nums)
        freq_list = []

        for key,val in freq_elem.items():
            freq_list.append([val,key])
        freq_list.sort(reverse=True)

        ans = []
        for i in range(k):
            ans.append(freq_list[i][1])
        

        return ans
    
        
