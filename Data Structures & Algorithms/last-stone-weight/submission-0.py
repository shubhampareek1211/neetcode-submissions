class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones)>1:
            x = stones.pop(0) # largest
            y = stones.pop(0) # 2nd largest

            if y!=x:
                stones.append(x-y)
                stones.sort(reverse=True)
        if stones:
            return stones[0]
        else:
            return 0 
             

        