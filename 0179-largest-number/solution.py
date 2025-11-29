class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        whole = []
        for num in nums:
            num = str(num)
            whole.append(num)
        print(whole)
        whole.sort(key=lambda x:x*12,reverse=True)
        ans = "".join(num for num in whole)
        return str(int(ans))

        
