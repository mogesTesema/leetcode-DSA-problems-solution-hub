class Solution:
    def isPalindrome(self, x: int) -> bool:
        isPalin=False
        if x<0:
            return False

        y=str(x)
        z=""
        l=len(y)
        for i in range(l):
            z+=y[l-i-1]
        y=int(z)
        if(x==y):
            isPalin=True
        return isPalin
        
        
