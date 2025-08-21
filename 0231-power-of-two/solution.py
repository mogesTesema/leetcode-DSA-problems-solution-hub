class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # x = log(n)/log(2)
        # if x==int(x):
        #     return True
        # else:
        #     return False
        if n==1:
            return True
        elif n <= 0:
            return False
        elif n % 2 != 0:
            return False
        else:
            return self.isPowerOfTwo(n/2)
