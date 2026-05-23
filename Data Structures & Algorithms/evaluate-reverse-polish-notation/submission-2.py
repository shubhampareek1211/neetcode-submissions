class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens:
            if i == "+":
                x = stk.pop()
                y = stk.pop()
                stk.append(int(y+x))
            elif i == "*":
                x = stk.pop()
                y = stk.pop()
                stk.append(int(y*x))
            elif i == "/":
                x = stk.pop()
                y = stk.pop()
                stk.append(int(y/x))
            elif i == "-":
                x = stk.pop()
                y = stk.pop()
                stk.append(int(y-x))
            else:
                stk.append(int(i))
        if len(stk)!=0:
            return stk[0]
        