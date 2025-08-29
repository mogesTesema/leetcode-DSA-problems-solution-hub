class Solution:
    def largestInteger(self, num: int) -> int:
        nums = [int(x) for  x in list(str(num))]
        odds = [x for x in nums if x%2 != 0]
        odds.sort(reverse=True)
        evens = [x for x in nums if x%2 == 0]
        evens.sort(reverse=True)
        # print(nums,"\n", odds,"\n", evens,)
        oddIndex = 0
        evenIndex = 0
        ans = []
        for digit in nums:
            if digit % 2 == 0:
                if evenIndex < len(evens):
                    ans.append(evens[evenIndex])
                    evenIndex += 1
                else:
                    ans.append(digit)
            else:
                if oddIndex < len(odds):
                    ans.append(odds[oddIndex])
                    oddIndex += 1
                else:
                    ans.append(digit)
        nums = "".join(map(str, ans))
        return int(nums)


