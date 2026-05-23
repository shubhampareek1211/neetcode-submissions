class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1
        mid = 0
        while l<=r:
            mid = l + (r-l)//2
            if target == nums[mid]:
                return True
            if nums[l]<nums[mid]:
                if nums[l]<=target<nums[mid]:
                    r = mid -1
                else:
                    l = mid +1
            elif nums[l] > nums[mid]:
                if nums[mid]<target<=nums[r]:
                    l = mid+1
                else:
                    r = mid -1 
            else:
                l +=1 # when we have equal l,m,r - worst case linear search 
        return False
        