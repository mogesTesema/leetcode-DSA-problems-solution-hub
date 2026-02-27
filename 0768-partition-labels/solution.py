class Solution:
    def partitionLabels(self, s):
        last = {}
        for i, c in enumerate(s):
            last[c] = i
        res = []
        start = 0
        end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res
