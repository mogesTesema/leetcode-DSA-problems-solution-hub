from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        p=defaultdict()
        
        for i,letter in enumerate(s):
            p[letter]=i

        farthest=0
        i=0
        j=0
        res=[]

        while j<len(s):
            farthest=p[s[i]]
            while i!=farthest:
                i+=1
                farthest=max(farthest,p[s[i]])
            res.append(farthest-j+1)
            j=i+1
            i+=1

        return res

            






