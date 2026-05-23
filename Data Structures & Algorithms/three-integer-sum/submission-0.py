class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, target in enumerate(nums):
            if i>0 and target ==nums[i-1]:
                continue
            l =i+1
            r = len(nums)-1
            while l < r:
                sum1 = target + nums[l] + nums[r]
                if sum1> 0:
                    r -=1
                elif sum1<0:
                    l +=1
                else:
                    ans.append([target,nums[l],nums[r]])
                    l +=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return ans
        
            