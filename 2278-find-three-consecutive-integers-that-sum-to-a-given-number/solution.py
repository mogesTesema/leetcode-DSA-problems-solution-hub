class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        smaller = num // 3
        remainder = num % 3 
        if remainder != 0:
            return []
        return [smaller -1, smaller,smaller +1]


        
        
