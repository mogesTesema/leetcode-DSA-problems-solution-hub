class Solution:
    def pancakeSort(self, arr):
        res = []
        n = len(arr)
        for size in range(n, 1, -1):
            max_idx = arr.index(max(arr[:size]))
            if max_idx + 1 != size:
                if max_idx != 0:
                    arr[:max_idx+1] = arr[:max_idx+1][::-1]
                    res.append(max_idx+1)
                arr[:size] = arr[:size][::-1]
                res.append(size)
        return res
