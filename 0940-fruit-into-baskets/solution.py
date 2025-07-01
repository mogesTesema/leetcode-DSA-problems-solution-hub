class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        right = 0
        maxLen = 0

        hashmap = {}

        while right < len(fruits):
            hashmap[fruits[right]] = hashmap.get(fruits[right], 0) + 1

            if len(hashmap) > 2:
                hashmap[fruits[left]] -= 1
                if hashmap[fruits[left]] == 0:
                    del hashmap[fruits[left]]
                left += 1

            maxLen = max(maxLen, right - left + 1)
            right += 1

        return maxLen
        
