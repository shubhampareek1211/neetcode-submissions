class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            count = [0]*26

            for c in s:
                count[ord(c)-ord("a")] +=1

            # conerting the list to a tuple so it can be used as dictionary key, as tuple are immutable 
            # here we want our keys to not change o/w type error would come

            key = tuple(count)

            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(s)

        return list(hashmap.values())