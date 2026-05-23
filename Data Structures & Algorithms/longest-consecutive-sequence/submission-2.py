class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        count = 0
        for i in my_set:
            if  (i - 1) not in my_set: # check if left neighbour exist in the number line
                l = 1 # start counting the sequence 
                while (i+l) in my_set:
                     l+=1
                count = max(l,count)
        return count
