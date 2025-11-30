class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        frq = Counter(arr1)
        

        answer = []
        excluded = []
        for arr2_num in arr2:
            current_nums = [arr2_num] * frq[arr2_num]
            answer.extend(current_nums)

        for arr1_num in frq:
            if arr1_num not in arr2:
                current_nums = [arr1_num] * frq[arr1_num]
                excluded.extend(current_nums)
        excluded.sort()
        answer.extend(excluded)
    
        return answer
