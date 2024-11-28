class Solution:
    def climbStairs(self, n: int) -> int:
        di = {}
        def sol(n):
            if (n==0):
                return 0
            if (n==1):
                return 1
            if(n not in di):
                ans = sol(n-1)+sol(n-2)
                di[n] = ans
                return ans
            else:
                return di[n]
        return sol(n+1)
        
