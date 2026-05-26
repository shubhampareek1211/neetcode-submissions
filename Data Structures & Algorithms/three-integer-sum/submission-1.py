class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,target in enumerate(nums):
            # not using same conscutive number again 
            if i>0 and target==nums[i-1]:
                continue 
            
            # 2 pointer approach 
            j = i+1
            k = len(nums)-1

            while j<k:
                sum1 = target + nums[j] + nums[k]
                if sum1 > 0:
                    k-=1
                elif sum1 < 0:
                    j+=1
                else:
                    res.append([target,nums[j],nums[k]])
                    j +=1
                    k -=1

                    # updating the pointer 
                    # move both pointer inward and 
                    # skip duplicates at the left pointer 
              
                    while nums[j] == nums[j-1] and j<k:
                        j +=1
        return res

                    

            
        