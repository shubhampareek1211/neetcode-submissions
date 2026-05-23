class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_pair = list(zip(position,speed))
        sorted_time_pair = sorted(time_pair,key=lambda x:x[0])
        stk = []
        for i,j in sorted_time_pair[::-1]:
            stk.append((target-i)/j)
            if len(stk) >=2 and stk[-1] <= stk[-2]:
                stk.pop()
        return len(stk)

        
