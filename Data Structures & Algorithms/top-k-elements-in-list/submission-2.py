class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] +=1
        
        res = []

        # storing the hashmap into array 

        for i,value in hashmap.items():
            res.append([value,i]) # value is stored first and then sort is performed on this

        res.sort()

        ans = []
        while len(ans) < k:
            ans.append(res.pop()[1])
        return ans
        




        