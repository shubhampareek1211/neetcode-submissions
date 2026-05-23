class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] += 1

        # mapping the number in the hashmap to the frequency group array
        # storing in the value, key format

        for key,value in hashmap.items():
            freq[value].append(key)
        
        res = []

        for i in range(len(freq)-1,0,-1): # -1 is for backward
            for key in freq[i]:
                res.append(key)
        # to stop the search when len(res) = k 
                if len(res) == k:
                    return res

        