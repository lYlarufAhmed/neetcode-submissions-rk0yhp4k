class MinHeap:
    
    def __init__(self):
        self.minHeap = [None]
        

    def push(self, val: int) -> None:
        self.minHeap.append(val)
        self._bubble_up(len(self.minHeap) - 1)



    def pop(self) -> int:
        if len(self.minHeap) == 1:
            return -1
        elif len(self.minHeap) == 2:
            return self.minHeap.pop()
        else:

            res = self.minHeap[1]
            self.minHeap[1] = self.minHeap.pop()

            self._bubble_down(1)
            return res
        

    def top(self) -> int:
        if len(self.minHeap) > 1: return self.minHeap[1]
        return -1
        

    def heapify(self, nums: List[int]) -> None:

        self.minHeap = [0] + nums

        for i in reversed(range(1, (len(self.minHeap) // 2 )+ 1)):
            self._bubble_down(i)


    def _bubble_up(self, index):
        parent = index // 2

        while index > 1 and self.minHeap[parent] > self.minHeap[index]:
            self.minHeap[parent], self.minHeap[index] = self.minHeap[index], self.minHeap[parent]

            index = parent
            parent = index // 2


    def _bubble_down(self, index):
        child = index * 2 # left

        while child < len(self.minHeap):
            if child + 1 < len(self.minHeap) and self.minHeap[child+1] < self.minHeap[child]:
                child += 1
            
            if self.minHeap[child] >= self.minHeap[index]: # already priority queue
                return
            
            self.minHeap[child], self.minHeap[index] = self.minHeap[index], self.minHeap[child]
            index = child
            child = index * 2
        
        