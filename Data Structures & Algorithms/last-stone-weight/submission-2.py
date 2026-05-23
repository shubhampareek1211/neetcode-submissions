class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # since python<3.14 only have min ; converting min to max by multiplying -1
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones)>1:
            first = heapq.heappop(stones) # negative of largest
            second = heapq.heappop(stones) # negative of 2nd largest

            if first!=second:
                heapq.heappush(stones,first- second) # keeping the negative
        if stones:
            return -stones[0] # last element will be negative
        else:
            return 0
            

        