class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # nums_dict = {val:index for index,val in enumerate(nums)}
        # print(f"original dictionary: {nums_dict}")
        # nums_tuples= list(nums_dict.keys())
        # print(f"value of dictionary:{keys}")
        # keys.sort()


        # nums_tuples =[]
        # for index, val in enumerate(nums):
        #     nums_tuples.append((val,index))
        # # print(nums_tuples)
        # nums_tuples.sort()
        # # print(nums_tuples)
        # left = 0 
        # right = len(nums_tuples) -1
        # while left < right:
        #     # print(f"left:{left},right:{right}")
        #     current_sum = nums_tuples[left][0] + nums_tuples[right][0] 
        #     # print(f"current_sum: {current_sum},targe:{target}")

        #     if current_sum == target:
        #         index_one = nums_tuples[left][1]
        #         index_two = nums_tuples[right][1]
        #         return [index_one,index_two]

        #     elif current_sum < target:
        #         left += 1

        #     else:
        #         right -= 1
        nums_dict =dict()
        for index, val in enumerate(nums):
            diff = target - val
            if diff in nums_dict:
                return [nums_dict[diff], index]
            else:
                nums_dict[val] = index
            

