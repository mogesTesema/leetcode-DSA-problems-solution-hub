class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def is_non_coprime(a,b):
            return math.gcd(a,b) >1
        stack = []
        for num in nums:
            curr = num
            while stack and is_non_coprime(curr, stack[-1]):
                curr = lcm(curr,stack.pop())
            stack.append(curr)
        return stack
