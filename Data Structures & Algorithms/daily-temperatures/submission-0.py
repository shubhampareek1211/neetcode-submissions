class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stk = [] # pair: [temp,index]
        for i,t in enumerate(temperatures):
            while stk and t > stk[-1][0]:
                stkvalue,stkindex = stk.pop()
                ans[stkindex] = i - stkindex
            stk.append((t,i))
        return ans

        