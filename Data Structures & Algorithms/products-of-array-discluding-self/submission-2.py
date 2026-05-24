class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        everything_before = 1
        everything_after = 1 
        
        for i in range(len(nums)):
            result[i] *= everything_before # product of all elements to the left
            # updating the prefix
            everything_before *=nums[i]
        # same for after 

        for i in range(len(nums)-1,-1,-1):
            result[i] *= everything_after
            everything_after *= nums[i]
        return result