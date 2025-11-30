from collections import deque

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        flips = 0
        op_count = 0
        q = deque()
        
        for i in range(n):
            if q and q[0] < i - 2:
                q.popleft()
                flips = 1 - flips
            
            cur = nums[i] if flips == 0 else 1 - nums[i]
            
            if cur == 0:
                if i + 2 >= n:
                    return -1
                op_count += 1
                flips = 1 - flips
                q.append(i)
        
        return op_count

