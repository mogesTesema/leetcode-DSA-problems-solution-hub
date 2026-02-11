class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:



        nums.sort()
        print(nums)
        ans = []

        pointer = 0

        while pointer < len(nums)-1:

            if nums[pointer] == nums[pointer+1]:
                ans.append(nums[pointer])
                pointer += 2
                continue
            pointer += 1
        return ans
            


        # nums_freq = Counter(nums)
        # ans = []

        # for key,val in nums_freq.items():
        #     if val == 2:
        #         ans.append(key)
        # return ans
       
        
