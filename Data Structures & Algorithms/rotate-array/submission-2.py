class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            n = k % len(nums)
            nums[:] = nums[:][::-1]
            nums[:n] = nums[:n][::-1]
            nums[n:]=nums[n:][::-1]
        else:
            nums[:] = nums[:][::-1]
            nums[:k] = nums[:k][::-1]
            nums[k:]=nums[k:][::-1]

        
        # # by 3 step reverse approach 
        
        # # reversing entire list 

        # nums[:] = nums[:][::-1]

        # # reversing all elements before k 
        # nums[:n] = nums[:n][::-1]

        # # reversing all elements after k 
        # nums[n:]=nums[n:][::-1]



        