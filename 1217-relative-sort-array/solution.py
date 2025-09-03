class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = defaultdict(int)
        for element in arr1:
            freq[element] = freq.get(element,0) + 1
        ans = []
        for element in arr2:

            ans.extend([element]*freq[element])
            freq[element] = 0
        unseen = []
        for item in freq:
            if freq[item] != 0:
                unseen.extend([item]*freq[item])
        unseen.sort()
        ans.extend(unseen)
        return ans
        
        
