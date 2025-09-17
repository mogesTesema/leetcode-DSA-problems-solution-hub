class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_dict = defaultdict(list)
        for word in strs:
            sorted_word = sorted(word)
            sorted_word = "".join(sorted_word)
            ans_dict[sorted_word].append(word)
        ans = []
        for value in ans_dict.values():
            ans.append(value)
        return ans

        

        
