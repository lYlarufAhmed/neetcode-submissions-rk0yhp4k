class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr = sorted(self.arr)
        

    def findMedian(self) -> float:
        l = len(self.arr)
        if l % 2:
            #odd
            p = l // 2
            return self.arr[p]
            pass
        else:
            #ven
            p = l // 2
            return (self.arr[p-1] + self.arr[p]) / 2
            pass
        
        