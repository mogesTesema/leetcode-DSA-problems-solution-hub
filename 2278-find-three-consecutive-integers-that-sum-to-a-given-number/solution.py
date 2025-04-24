class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        remain = num %3
        if remain != 0:
            return []
        else:
            r = num//3
            return [r-1,r,r+1]
