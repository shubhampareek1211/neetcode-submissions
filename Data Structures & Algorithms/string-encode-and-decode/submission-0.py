class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for i in strs:
            st += str(len(i))+ "#" + i
        return st

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!= "#":
                j += 1
            length = int(s[i:j])
            i = j+ 1
            j = i +length
            result.append(s[i:j])
            i = j
        return result
            
