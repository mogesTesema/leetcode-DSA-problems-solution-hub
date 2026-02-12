class Solution:
    def frequencySort(self, s: str) -> str:
        str_freq = Counter(s)
        freq_counted= []
        for key,val in str_freq.items():
            freq_counted.append([val,key])
        

        freq_counted.sort(reverse=True)
        ans = ""

        for val,key in freq_counted:
            ans += val*key
        
        return ans

