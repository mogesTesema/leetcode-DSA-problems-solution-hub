class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        index_nums = [[num,index] for index,num in enumerate(nums)]
        index_nums.sort()
        counter = 0
        prev = index_nums[0][0]
        ans = [0]*len(index_nums)


        for i in range(len(index_nums)):
            val = index_nums[i][0]
            index = index_nums[i][1]

            if val == prev:
                ans[index] = counter
                continue

            ans[index] = i
            prev = val
            counter = i



        return ans


        
