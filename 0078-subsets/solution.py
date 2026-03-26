class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = [[]]

        def backtrack(index,sub):


            for elem in range(index,len(nums)):

                if nums[elem] in sub:
                    continue
                sub.add(nums[elem])
                sub_ans = list(sub)[:]
                sub_ans.sort()
                if not sub_ans in ans:
                    ans.append(sub_ans)
                backtrack(index+1,sub)
                sub.remove(nums[elem])
        backtrack(0,set())
        return ans

