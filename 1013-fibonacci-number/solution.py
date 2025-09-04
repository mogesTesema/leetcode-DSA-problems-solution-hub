class Solution:
    def __init__(self):
        self.fibValues = {}
    def fib(self, n: int) -> int:

        # if n == 1: return 1
        # if n == 0: return 0
        # if n in self.fibValues: return self.fibValues[n]
        # untracked = self.fib(n-1) + self.fib(n-2)
        # self.fibValues[n] = untracked
        # return untracked
        
        memo = defaultdict(int)
        
        def fib(n):
            if n == 0: return 0
            if n == 1: return 1
            if n not in memo:
                memo[n] = fib(n-1) + fib(n-2)
            return memo[n]
        return fib(n)
    
        
