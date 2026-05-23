class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        ans = nums[0]
        while l<=r:
            if nums[l]<nums[r]: # the whole looking element might be sorted 
                ans = min(nums[l],ans)
                break
            mid = (l+r)//2
            if nums[l] <= nums[mid]: # then the left part is useless 
                l = mid+1
                ans = min(nums[mid],ans)
                
            else:
                r = mid-1
                ans = min(nums[mid],ans)
                
        return ans

        