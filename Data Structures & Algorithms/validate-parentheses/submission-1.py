class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        bracket_hashmap = {")":"(", "]":"[","}":"{"}
        for i in s:
            if i in bracket_hashmap:
                if stk and stk[-1] == bracket_hashmap[i]:
                    stk.pop()
                else:
                    return False

            else:
                stk.append(i)

        if len(stk)==0:
            return True
        else:
            return False
    
        
        