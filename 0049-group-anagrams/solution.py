class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        anagrams = {}

        for index,word in enumerate(strs):

            word = list(word)
            word.sort()
            word = "".join(word)

            if word in anagrams:
                anagrams[word].append(strs[index])
            else:
                anagrams[word] = [strs[index]]



        ans = []

        for val in anagrams.values():
            ans.append(val)
            
        
        return ans

    
         
        
