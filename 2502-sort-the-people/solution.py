class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # for i in range(len(names)-1):
        #     for j in range(0, len(names)-i-1):
        #         if heights[j]<heights[j+1]:
        #             heights[j],heights[j+1]= heights[j+1], heights[j]
        #             names[j], names[j+1] = names[j+1], names[j]
        # return names
        nameh = dict()
        for i in range(len(names)):
            nameh[heights[i]] = names[i]
        name = sorted(nameh.keys(), reverse=True)
        print(nameh)
        print(name)
        ans = []
        for item in name:
            
            ans.append(nameh[item])
        return ans





        
