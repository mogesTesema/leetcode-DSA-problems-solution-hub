class Solution:
    def myPow(self, x: float, n: int) -> float:

        # store already comuted power in the cache, don't repeat yourself!
        precomputed = {}

        # handle cases where n == 0
        if n == 0:
            return 1
        
        # handle cases where n < 0
        if x == 0:
            return 0

        """
        divide the power into to equivalent power and then computed for each power recursively.
        using the cached result, if not compute and put in some cache.
        """
        def recursion_power(curr_power):

            if curr_power == 1:
                return x
            
            # use cached result, DRY princple
            if curr_power in precomputed:
                return precomputed[curr_power]

            else:
                # divide the power into two somehow equal integer, compute powers and put into cache
                left_power = curr_power//2
                right_power = left_power + (curr_power % 2)
                curr_computed =  recursion_power(left_power) * recursion_power(right_power)
                precomputed[curr_power] = curr_computed

            return precomputed[curr_power]




        positive_power = abs(n)
        ans = recursion_power(positive_power)

        # handle for power is positive number
        if n > 0:
            return ans
        #handle for power is negative, it going to be 1/ans
        else:
            return 1/ans

