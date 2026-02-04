class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []
        for  interval in intervals:
            if len(stack) == 0:
                stack.append(interval)
            else:
                top = stack.pop()
                if top[1] >= interval[0]:
                    stack.append([top[0],max(top[1],interval[1])])
                else:
                    stack.append(top)
                    stack.append(interval)
    
        return stack
                
                
                


































        # print(intervals)
        # ans = []
        # if len(intervals) == 1:
        #     return intervals
        # for i in range(len(intervals)-1):
        #     first_interval = intervals[i]
        #     second_interval = intervals[i+1]
        #     if first_interval[1] >= second_interval[0]:
        #         ans.append([first_interval[0],max(first_interval[1],second_interval[1])])
        #     else:
        #         if len(ans) == 0:
        #             ans.append(first_interval)
        #         ans.append(second_interval)

        # print(ans)
        # return ans





        
       
