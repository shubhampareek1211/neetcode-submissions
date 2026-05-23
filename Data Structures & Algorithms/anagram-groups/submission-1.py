class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in strs:
            count = [0] * 26 # creating a count array of 26 size a-z
            for j in i:
                count[ord(j)-ord('a')] += 1
            res[tuple(count)].append(i)
        return list(res.values())
        