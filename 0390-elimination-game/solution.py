class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1
        
        return 2 * (n // 2 + 1 - self.lastRemaining(n // 2))

# class Solution:
#     def lastRemaining(self, n: int) -> int:
        
#         flag = True
#         n = list(range(1,n+1))
#         new_arr = []

#         while len(n) > 1:

#             new_arr = []

#             if flag:
#                 for i in range(1,len(n),2):
#                     new_arr.append(n[i])
#                 flag=False
#             else:
#                 for i in range(len(n)-2,-1,-2):
#                     new_arr.append(n[i])
#                 new_arr.reverse()

#                 flag=True

#             n = new_arr

#         return n[-1]
