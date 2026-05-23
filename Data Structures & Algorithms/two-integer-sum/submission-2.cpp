class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map <int,int> mpp;
        for(int i=0;i<n;i++){
            int diff = target - nums[i];
            if(mpp.find(diff)!=mpp.end()){ // != if it equals to the diff
                return {mpp[diff],i}; // mpp[diff] return hashmap index and i return normal
            }
            mpp[nums[i]] = i;
        }
        return {};
    }
        
};
