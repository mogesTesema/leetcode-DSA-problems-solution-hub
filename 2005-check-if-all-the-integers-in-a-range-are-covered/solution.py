class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # def in_range(num):
        #     for interval in ranges:
        #         if interval[0] <= num <= interval[1]:
        #             return True
        #     return False
        # inclusive = {i for i in range(left,right+1)}
        
        # for num in inclusive:
        #     if not in_range(num):
        #         return False
        # return True

        nums = set(range(left,right+1))

        for num in ranges:
            nums -= set(range(num[0],num[1]+1))
        
        return True if nums == set() else False
        

