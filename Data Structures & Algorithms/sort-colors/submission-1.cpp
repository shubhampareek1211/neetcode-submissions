class Solution {
public:
    void sortColors(vector<int>& nums) {
        if(nums.empty()) return;
        int n = nums.size()-1;
        int low = 0;
        int right = n;
        int mid = 0;
        while(mid<=right){
            if(nums[mid]==0) {
                swap(nums[low],nums[mid]);
                low++;
                mid++;
            }
            else if(nums[mid]==1) mid++;
            else{
                swap(nums[mid],nums[right]);
                    right--;
                
            }
    

    }
    }

};