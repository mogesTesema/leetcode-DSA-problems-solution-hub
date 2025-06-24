class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatingSpeed():
            slow = 1
            fast = max(piles)
            while slow <= fast:
                mid = (slow + fast)//2
                if validate(mid):
                    fast = mid - 1
                else:
                    slow = mid + 1
                print((slow,fast), end= " ")

            return slow
        def validate(speed):
            current_hour = 0
            for bananas in piles:
                current_hour += ceil(bananas/speed)
                if current_hour > h:
                    return False
            return True
        return eatingSpeed()
