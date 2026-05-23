class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashmap1 = {}
        hashmap2 = {}

        for i in range(len(s)):
                hashmap1[s[i]] = 1 + hashmap1.get(s[i],0) 
                # the get function makes sure we can get around if key don't exist and give default value 
                hashmap2[t[i]] = 1 + hashmap2.get(t[i],0)
        
        for j in hashmap1:
            if hashmap1[j] != hashmap2.get(j,0):
                return False
        return True