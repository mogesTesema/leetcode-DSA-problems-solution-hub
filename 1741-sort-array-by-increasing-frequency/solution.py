class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        # a: count frq value of each num
        frq = defaultdict()
        for num in nums:
            num = -1 * num # negate the element for the seek of sorting in increase order
            frq[num] = frq.get(num,0) + 1


        # b: make num opposive sign of its original version
        # c: swap the frequency and value
        frq = list([value, key] for key, value in frq.items())

        # d: sort the latest version of frq
        frq.sort()


        # e: restore the original nums while keeping new order
        nums = []
        for frq, val in frq:
            current_nums = [-1*val]*frq # respore the original element after performing sorting.
            nums.extend(current_nums)

            
        # f: DONE submit the result
        return nums





        
        
