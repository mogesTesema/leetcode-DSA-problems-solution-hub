class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        # ans = sorted(freq, lambda x: freq[x])
        ans = sorted(freq.items(),key=lambda x:x[1],reverse=True)
        max_freq = ans[0][1]
        counter = 0
        for item in ans:
            if item[1]==max_freq:
                counter += 1
            else:
                break
        return max_freq*counter
        
     
        
