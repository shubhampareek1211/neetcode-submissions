class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = {}
        x = 0
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] +=1

        for i,j in hashmap.items():
            if j>1:
                return i
    
        
        