class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def xSum(arr):
            frq = defaultdict()
            for item in arr:
                frq[item] = frq.get(item,0)+1
            arr = []
            for val, fr in frq.items():
                arr.append((fr,val))
            heapify(arr)
            arr = nlargest(x,arr)
            xsum = 0
            for fr, val in arr:
                xsum += fr*val
            return xsum
        
        ans = []
        for i in range(len(nums)-k+1):
            xsum = xSum(nums[i:k+i])
            ans.append(xsum)
        return ans
        
