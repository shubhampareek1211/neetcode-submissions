class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k 
        heapq.heapify(self.minHeap) # inserting array to turn into min-heap in linear time
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) # pop and return the smallest item from heap and mainting the min-heap
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val) # pushing val into heap and maintaing min-heap invaraint
        if len(self.minHeap) >self.k:
            heapq.heappop(self.minHeap) # removes the min ele in min heap which is root
        return self.minHeap[0] # smallest element is the kth largest element
        
