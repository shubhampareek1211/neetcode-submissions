class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0 
        distance = 0 
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l +=1
            charset.add(s[r])
            distance = max(distance,r - l + 1)
        return distance
        