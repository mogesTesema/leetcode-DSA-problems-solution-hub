class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def find_min(arr,x): 
            low = 0
            high = len(arr) - 1

            while low <= high:
                mid = (low + high) // 2
                if arr[mid] >= x:  
                    high = mid - 1    
                else:
                    low = mid + 1     
            return low

            
        potions.sort()
        ans = []
        for num in spells:
            min_value = success/num
           
            left = find_min(potions,min_value)
            if left == len(potions):
                ans.append(0)
            else:
                ans.append(len(potions)-left)
        return ans

