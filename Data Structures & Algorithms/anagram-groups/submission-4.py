class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        value_dict = {} # empty dictinoary 
        if not strs:
            return list(strs)
        for word in strs:
            key = "".join(sorted(word))  # sorts the character alone and join to form word
            if key not in value_dict:
                value_dict[key] = []
            value_dict[key].append(word) # [act: act,cat]
        return list(value_dict.values())