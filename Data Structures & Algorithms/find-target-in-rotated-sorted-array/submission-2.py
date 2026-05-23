class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[l] <= nums[mid]: # left half is sorted array
                if nums[l]<= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid +1
            else:
                if nums[mid] < target <= nums[r]: # target in sorted right half, checking the whole range
                    l = mid +1
                else:
                    r = mid -1

            if target == nums[mid]:
                return mid 
        return -1
        