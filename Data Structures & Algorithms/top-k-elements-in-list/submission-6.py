class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = []
        for _ in range(len(nums)+1): # so that we have n+1 index array
            freq.append([]) 
        # simpler pythonic way freq [[] for i in range(len(nums)+1)]

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] +=1 
        
        # now mapping the value and key to freq array as value -> index and key as freq index value

        for i,v in hashmap.items():
            freq[v].append(i)

        # now we want top k elements and we travese from back and return values which exist as top k 

        result = []

        i = len(freq) -1
        while i>=0 and k>0:
            if freq[i]: # check if bucket list of list is empty or not
                for num in freq[i]:
                    result.append(num)
                    k -=1
                    if k==0:
                        return result
            i -=1
        return result

            
