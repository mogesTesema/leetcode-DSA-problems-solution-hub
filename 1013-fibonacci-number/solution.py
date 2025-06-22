class Solution:
    def __init__(self):
        self.fibValues = {}
    def fib(self, n: int) -> int:
        if n == 1: return 1
        if n == 0: return 0
        if n in self.fibValues: return self.fibValues[n]
        untracked = self.fib(n-1) + self.fib(n-2)
        self.fibValues[n] = untracked
        return untracked
    
        
