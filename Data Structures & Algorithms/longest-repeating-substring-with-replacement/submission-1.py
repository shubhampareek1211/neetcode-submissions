class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        maxf = 0
        hashmap = {}
        ans = 0
        for r in range(len(s)):
            if s[r] not in hashmap:
                hashmap[s[r]] = 0
            hashmap[s[r]] += 1
            maxf = max(maxf,hashmap[s[r]])
# to check if the window is valid otherwise trim down
            while (r-l+1) - maxf > k:
                # trim down 
                hashmap[s[l]] -=1
                l +=1 
            ans = max(ans,r-l+1)
        return ans

        