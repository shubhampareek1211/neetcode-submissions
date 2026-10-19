class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums1 = [0] * n 
        for i in range(len(nums)):
            nums1[i] = (target - nums[i])

        for i in range(n):
            for j in range(n):
                if nums[i]==nums1[j] and i!=j:
                    return [i,j]
            
         


        