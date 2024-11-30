class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        def alreadyIn(arr, anslist):
            for ele in anslist:
                if arr == ele:
                    return True
            return False
                

        dp = defaultdict(list)

        for ele in candidates:
            dp[ele].append([ele])

        for i in range(target + 1):
            for c in candidates:
                if i - c >= 0:
                    for comb in dp[i-c]:
                        temp = comb + [c]
                        temp.sort()
                        if alreadyIn(temp, dp[i]):
                            continue
                        else:
                            dp[i].append(temp)

        return dp[target]
