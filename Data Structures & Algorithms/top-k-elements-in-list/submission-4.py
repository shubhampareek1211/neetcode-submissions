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
        
        # check the output via print - it's stored like a bucket 

        result = []
        # looping in the reverse direction 
        for i in range(len(freq)-1,0,-1):
            for element in freq[i]:
                result.append(element)
                # stopping condition when the appended element = k 
                if len(result) == k:
                    return result



        