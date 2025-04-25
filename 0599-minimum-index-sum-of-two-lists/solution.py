class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        least_indexs = 0
        temp = 0
        answer = []
        for l in list1:
            if l in list2:
                temp = list1.index(l) + list2.index(l)
                if temp < least_indexs:
                    answer.clear()
                    answer.append(l)
                elif temp == least_indexs:
                    answer.append(l)
                if temp > least_indexs and len(answer) ==0:
                    least_indexs = list1.index(l) + list2.index(l)
                    answer.append(l)
        return answer



