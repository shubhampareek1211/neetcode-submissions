from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap way, equal number of characters 
        # base case
        if len(s)!=len(t):
            return False
        hashmap1 = Counter(s)
        hashmap2 = Counter(t)
        if hashmap1 == hashmap2:
            return True
        
        return False