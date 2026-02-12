class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:

        unduplicated = []

        for response in responses:
            unduplicated.append(list(set(response)))

        # print(unduplicated)

        response_freq = {}

        for response in unduplicated:
            for comment in response:
                if comment in response_freq:
                    response_freq[comment] += 1
                else:
                    response_freq[comment] = 1
        ans = []

        for key,val in response_freq.items():
            ans.append([val,key])
        ans.sort(reverse=True)
        # print(f"ans:{ans}")


        if len(ans) == 1:
            return ans[0][1]
        if ans[0][0] > ans[1][0]:
            return ans[0][1]
        candidate = []
        base = ans[0][0]

        for freq,val in ans:
            if freq == base:
                candidate.append(val)
            else:
                break
        candidate.sort()
        return candidate[0]
       
        
