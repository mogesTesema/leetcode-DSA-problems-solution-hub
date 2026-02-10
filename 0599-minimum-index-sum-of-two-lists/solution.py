class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:


        list1_set = set(list1)
        list2_set = set(list2)
        common = list1_set & list2_set
        ans = []
        least_index = float("inf")

        for chars in common:
            index_one = list1.index(chars)
            index_two = list2.index(chars)
            index_sum = index_one + index_two

            if index_sum < least_index:
                ans = [chars]
                least_index = index_one + index_two
            elif index_sum == least_index:
                ans.append(chars)
        return ans


        
