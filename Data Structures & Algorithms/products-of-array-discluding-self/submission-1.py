class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        list_p = [0]* n
        list_s = [0]*n
        result = [0]*n
        # initalising first and last value as 1 for prefix and suffix 
        list_p[0]=1
        list_s[n-1]=1

        for i in range(1,n):
            list_p[i] = nums[i-1]* list_p[i-1]
        
        for i in range(n-2,-1,-1): # travesing from back to fill the array
            list_s[i] = nums[i+1]*list_s[i+1]

        for i in range(n):
            result[i] = list_p[i]*list_s[i]
        
        return result
        