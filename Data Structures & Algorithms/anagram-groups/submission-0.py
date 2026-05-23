class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        ans = []
        for i in strs:
            sorted_list = ''.join(sorted(i))

            if sorted_list not in hashmap:
                hashmap[sorted_list] = []
            hashmap[sorted_list].append(i)
        
        return list(hashmap.values())

        