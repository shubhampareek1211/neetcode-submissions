class Solution {
public:
    void sortColors(vector<int>& nums) {

        if(nums.size()<1) return;

        int red = 0;
        int blue = 0;
        int white = 0;

        for(int i=0;i<nums.size();i++){
            if(nums[i]==1) blue++;
            if(nums[i]==0) red++;
            if(nums[i]==2) white++;
        }
        for(int i=0;i<red;i++){
            nums[i] = 0;
        } 
        for(int i=red;i<(red+blue);i++) nums[i] =1;
        for(int i=red+blue;i<(red+blue+white);i++) nums[i]=2;
    
    }

};