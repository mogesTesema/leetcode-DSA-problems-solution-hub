class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        heapify(self.minheap)
        heapify(self.maxheap)
        

    def addNum(self, num: int) -> None:
        heappush(self.maxheap, -num)
        heappush(self.minheap, -1*heappop(self.maxheap))
        if len(self.minheap) > len(self.maxheap):
            heappush(self.maxheap, -1*heappop(self.minheap))

        

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] + (-1)*self.maxheap[0])/2
        else:
            return -1*self.maxheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
