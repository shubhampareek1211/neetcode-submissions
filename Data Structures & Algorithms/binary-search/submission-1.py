class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) 
        i = 0
        j = n -1
        mid = 0
        while i <= j:
            mid = (i+j)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                i = mid+1 
            else:
                j = mid-1
        return -1