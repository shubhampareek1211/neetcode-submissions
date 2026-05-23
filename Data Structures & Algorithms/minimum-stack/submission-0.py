class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)

    def pop(self) -> None:
        self.stk.pop()
        

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        ans = []
        min_e = self.stk[-1]
        while len(self.stk):
            min_e = min(self.stk[-1],min_e)
            ans.append(self.stk.pop())
        for i in range(len(ans))[::-1]:
            self.stk.append(ans[i])
        return min_e
            
        
