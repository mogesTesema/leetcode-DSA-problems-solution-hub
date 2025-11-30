class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
       
        stack = []
        answer = prices[:]
        for idx, price in enumerate(prices):

            if stack and price <= stack[-1][0]:
                curr_price = stack[-1][0]
                while stack and price <= stack[-1][0] :
                    curr_price,curr_index = stack.pop()
                    pay = curr_price - price
                    answer[curr_index] = pay
                stack.append([price,idx])
            else:
                stack.append([price,idx])
            
        while stack:
            curr_price,curr_index = stack.pop()
            answer[curr_index] = curr_price

        return answer




