class Solution:
    def reverse(self, x: int) -> int:
        """
        -2,147,483,648, and the maximum value is 2,147,483,647
        """
        isPositive = True if x >= 0 else False
        final_num = None
        str_version = None
        if isPositive:
            str_version = str(x)[::-1]
            final_num = int(str_version)
            if final_num <= (2**31 - 1):
                return final_num
            else:
                return 0
        else:
            str_version = str((-1)*x)[::-1]
            final_num = (-1) * int(str_version)
            if final_num >= -2**31:
                return final_num
            else:
                return 0

        
            

        
