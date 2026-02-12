class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        even_store = []
        even_sum = 0

        def is_even(num):
            return True if num %2 == 0 else False
        


        ans = []

        for num in nums:
            if is_even(num):
                even_store.append(num)
                even_sum += num


        for query in queries:
            val,index = query
            curr_num = nums[index]
            
            if is_even(curr_num):
                if is_even(curr_num+val):
                    even_sum += val
                else:
                    even_sum -= curr_num
                nums[index] += val
            else:
                if is_even(curr_num+val):
                    even_sum += val + curr_num
                else:
                    pass
                nums[index] += val
            ans.append(even_sum)
        return ans







