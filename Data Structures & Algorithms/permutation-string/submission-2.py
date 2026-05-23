class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hashmap = {}
        for i in range(len(s1)):
            if s1[i] not in hashmap:
                hashmap[s1[i]] = 0
            hashmap[s1[i]] +=1
        l = 0
        r = len(s1)
        while r <= len(s2):
            hashmap2 = {}
            for i in range (l,r):
                if s2[i] not in hashmap2:
                    hashmap2[s2[i]] = 0
                hashmap2[s2[i]] += 1
            # comparing the 2 hashmap current value
            if hashmap2 ==  hashmap:
                return True
    
            l += 1 
            r += 1 
        return False

        