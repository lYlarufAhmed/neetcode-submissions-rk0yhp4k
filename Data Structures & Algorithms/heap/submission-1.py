class MinHeap:
    
    def __init__(self):
        self.minHeap = [None]
        

    def push(self, val: int) -> None:
        self.minHeap.append(val)

        if len(self.minHeap) > 1:

            #bubble up
            curr = len(self.minHeap) - 1

            while curr > 1 and self.minHeap[curr] < self.minHeap[curr//2]:
                self.minHeap[curr], self.minHeap[curr//2] = self.minHeap[curr//2], self.minHeap[curr]
                curr = curr//2



    def pop(self) -> int:
        if len(self.minHeap) == 1:
            return -1

        elif len(self.minHeap) == 2:
            return self.minHeap.pop()
        else:

            res = self.minHeap[1]
            self.minHeap[1] = self.minHeap.pop()

            i = 1

            while 2*i < len(self.minHeap):
                if (2*i+1 < len(self.minHeap)) and self.minHeap[2*i + 1] < self.minHeap[2*i] and self.minHeap[i] > self.minHeap[2*i+1]:
                    self.minHeap[i] , self.minHeap[2*i + i] = self.minHeap[2*i+1], self.minHeap[i]
                    i = 2 * i +1
                elif self.minHeap[i] > self.minHeap[2*i]:
                    self.minHeap[i], self.minHeap[2*i] = self.minHeap[2*i], self.minHeap[i]
                    i = 2 * i
                else:
                    break
            return res
        pass
        return -1
        

    def top(self) -> int:
        if len(self.minHeap) > 1: return self.minHeap[1]
        return -1
        

    def heapify(self, nums: List[int]) -> None:

        for num in nums:
            self.push(num)
        
        