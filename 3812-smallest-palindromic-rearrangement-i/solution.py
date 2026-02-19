class Solution:
    def smallestPalindrome(self, s: str) -> str:

        char_counted = Counter(s)
        s = list(set(s))
        s.sort()

        ans = ""
        odd = ""
        for char in s:
            val = char_counted[char]
            if val %2 == 0:
                ans += char*(val//2)
            else:
                ans += char*(val//2)
                odd+=char*(val%2)
        final_ans = ans + odd + ans[::-1]

        return final_ans
            

       


        # while cp<len(check):
        #     if char_counted[check[cp]]%2==0:
        #         while char_counted[check[cp]]>0:
        #             ans[l]=check[cp]
        #             ans[r]=check[cp]
        #             l+=1
        #             r-=1
        #         cp+=1
        #     else:
        #         while char_counted[cp]>0:
        #             ans[l]=char_counted[cp]
        #             l+=1
        #         cp+=1
        #     return "".join(ans)



        








        
