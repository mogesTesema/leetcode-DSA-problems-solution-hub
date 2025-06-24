class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def leastWeight():
            low = max(weights)
            high = sum(weights)
          
            while low <= high:
                mid = (low + high)//2
                if validate(mid):
                 
                    high = mid - 1
                else:
                    low = mid + 1
                
            return low
        def validate(capacity):
            day_counter = 1
            currentWeight = 0
            for weight in weights:
                currentWeight += weight
                if currentWeight > capacity:
                    day_counter += 1
                    currentWeight = weight
                    if day_counter > days:
                        return False
            return True
        return leastWeight()
            
