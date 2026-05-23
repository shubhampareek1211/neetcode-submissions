class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_string = ''.join(sorted(s1))
        for i in range(len(s2)):
            for j in range(i,len(s2)):
                sorted_string2 = ''.join(sorted(s2[i:j+1]))
                if sorted_string == sorted_string2:
                    return True
                
        return False
        