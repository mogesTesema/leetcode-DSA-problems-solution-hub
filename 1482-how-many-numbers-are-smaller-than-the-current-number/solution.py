class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # answer = []
        # for i in range(len(nums)):
        #     counter =0
        #     for j in range(len(nums)):
        #         if nums[j]<nums[i]:
        #             counter +=1
        #     answer.append(counter)
        # return answer
        arr = sorted(nums)
        result = dict()
        for i, val in enumerate(arr):
            if val not in result:
                result[val] = i
        ans = []
        for i in nums:
            ans.append(result[i])
        return ans
