class Solution:
    def mySqrt(self, x: int) -> int:
        res = 1
        if x<=1:
            return x
        for i in range(0,x//2+1):
            if i*i<=x:
                res = i
                continue
            else:
                res = i -1
                break
        return res

