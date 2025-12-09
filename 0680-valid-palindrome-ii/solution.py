class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        has_deleted = False
        def palind(left,right):
            while left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    nonlocal has_deleted
                    if has_deleted:
                        return False
                    has_deleted = True
                    return palind(left+1,right) or palind(left, right -1)
                
                
            return True

        return palind(left,right)
