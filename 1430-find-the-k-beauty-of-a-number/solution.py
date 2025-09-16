class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        string_num = str(num)
        counter = 0
        for i in range(len(string_num)-k +1):
            n = string_num[i:i+k]
            n = int(n)
            if n == 0:
                continue
            if num % n == 0:
                counter += 1
        return counter

        
