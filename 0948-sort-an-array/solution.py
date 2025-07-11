class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arrOne, arrTwo):
            #using selection sort
            leftOne =0
            leftTwo =0
            arr = []  
            while leftOne < len(arrOne) and leftTwo < len(arrTwo):
                if arrOne[leftOne] < arrTwo[leftTwo]:
                    arr.append(arrOne[leftOne])
                    leftOne += 1
                else:
                    arr.append(arrTwo[leftTwo])
                    leftTwo += 1
            arr.extend(arrOne[leftOne:])
            arr.extend(arrTwo[leftTwo:])
            return arr
        
        def mergeSort(left,right,arr):
            if left == right:
                return [arr[left]]
            mid = (left + right)//2
            leftArr = mergeSort(left,mid,arr)
            rightArr = mergeSort(mid+1,right,arr)
            return merge(leftArr,rightArr)
        return mergeSort(0,len(nums)-1,nums)
