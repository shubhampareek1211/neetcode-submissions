class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            hashmap[i] +=1
        # sorting keys based on their values(freq) in desc order

        sorted_ele = sorted(hashmap.keys(),key=hashmap.get,reverse=True)

        return sorted_ele[:k]