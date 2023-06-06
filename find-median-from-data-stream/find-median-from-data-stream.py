from heapq import *
class MedianFinder:

    def __init__(self):
        self.min_heap_large = []
        self.max_heap_small = []
        self.len = 0

    def addNum(self, num: int) -> None:
        # add number to smaller half
        heappush(self.max_heap_small, -1*num)

        print()
        # add biggest number in smaller half to bigger half
        heappush(self.min_heap_large, -1*heappop(self.max_heap_small))

        if len(self.min_heap_large) > len(self.max_heap_small):
            heappush(self.max_heap_small, -1*heappop(self.min_heap_large))

        self.len += 1


    def findMedian(self) -> float:

        

        if self.len % 2 != 0:
            return -1 * self.max_heap_small[0]
        
        return (-1 * self.max_heap_small[0] + self.min_heap_large[0]) / 2
        

# if array alweays sorted, it is ease

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()