class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counted_elem = Counter(nums)

        for key in counted_elem:
            if counted_elem[key] > len(nums)/2:
                return key

        
            



        
