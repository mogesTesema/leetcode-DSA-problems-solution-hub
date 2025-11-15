class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = []
        arr_set = set(arr)
        max_value = max(arr)
        missed_nums = []
        for i in range(1,max_value+1):
            if i not in arr_set:
                missed_nums.append(i)
        if k <= len(missed_nums):
            return missed_nums[k-1]
        else:
            return arr[-1] + k-len(missed_nums)
        
    
