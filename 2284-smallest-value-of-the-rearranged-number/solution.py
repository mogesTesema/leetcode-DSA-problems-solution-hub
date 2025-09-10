
class Solution:
    def smallestNumber(self, num: int) -> int:
        # Handle zero quickly
        if num == 0:
            return 0
        
        is_negative = num < 0
        digits = list(str(abs(num)))
        
        if is_negative:
            # For negative, sort digits in descending order (max absolute value for smallest negative)
            digits.sort(reverse=True)
            return -int("".join(digits))
        else:
            # For positive, sort digits in ascending order
            digits.sort()
            # Find first non-zero digit to avoid leading zeros
            for i, d in enumerate(digits):
                if d != '0':
                    # Swap first non-zero digit to front
                    digits[0], digits[i] = digits[i], digits[0]
                    break
            return int("".join(digits))
