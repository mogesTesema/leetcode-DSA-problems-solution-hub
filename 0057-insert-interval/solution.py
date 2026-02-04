class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        1.find the exact place where newInterval going to be inserted
            a. brute force
                newinterval[0] <= interval[1]
        2. make sure interals are not overlapping if so, merge

        """
        intervals.append(newInterval)
        intervals.sort()
        def merge(arry):
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
        return merge(intervals)
        
        # for i in  range(len(intervals)):
        #     if newInterval[0] <= intervals[i][1]:
        #         intervals[i][1] = max(newInterval[1],intervals[i][1])
        #         print("intevals",intervals)
        #         break
        #         # merged = merge(intervals[i:])
        #         # return intervals[:i] + merged
        # return (merge(intervals))



        
