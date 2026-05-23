class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            # sorted string as unique key
            sortedstring = ''.join(sorted(i))
            # if key don't exist then in values we want a list
            if sortedstring not in hashmap:
                hashmap[sortedstring] = []
            hashmap[sortedstring].append(i)
        return list(hashmap.values())
        