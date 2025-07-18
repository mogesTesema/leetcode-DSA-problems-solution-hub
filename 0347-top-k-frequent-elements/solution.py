class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = dict()
        ans = []
        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1
        hash_table = sorted(hash_table.items(),key= lambda item :item[1],reverse=True)
       
        for i in range(k):
            ans.append(hash_table[i][0])
        return ans

                
        
