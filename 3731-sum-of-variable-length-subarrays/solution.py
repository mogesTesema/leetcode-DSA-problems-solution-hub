class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        nums_copy = []
        for index in range(len(nums)):
            nums_copy.append(nums[index])
            if index == 0:
                continue
            nums[index] = nums[index] + nums[index-1]
        answer = []
        for i in range(len(nums)):
            start = max(0, i -nums_copy[i])
            if start == 0:
                answer.append(nums[i])
            else:
                answer.append(nums[i]-nums[start-1])
        return sum(answer)
