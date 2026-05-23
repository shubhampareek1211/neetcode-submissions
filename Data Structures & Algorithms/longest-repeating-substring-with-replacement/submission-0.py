class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        for i in range(len(s)):
            count = 0 
            hashmap = {}
            for j in range(i,len(s)):
                # keeping the count in hashmap
                if s[j] not in hashmap:
                    hashmap[s[j]] = 0
                hashmap[s[j]] +=1
                count = max(count,hashmap[s[j]]) # to track the most frequent char in window and hashmap 
                # using this equation 
                # windowLength - count["char"] < = k 
                if (j-i+1) - count <= k: # no of possible replacement in the window 
                    ans = max(j-i+1,ans) # calculate the window length counter
                # else i++ and loop breaks when j reaches the len(s)-1
        return ans


                

        