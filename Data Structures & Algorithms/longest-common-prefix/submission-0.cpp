class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()){
         return "";
        }
        string result = "";
       sort(strs.begin(),strs.end());
       /* comparing the first and the last element to get the biggest continous array */
       
       string s_first = strs[0];
       string s_last = strs.back();

      
       for(int i=0;i<s_first.size();i++){
        if(s_first[i]!=s_last[i]){
            break;
        }
        else
        result += s_first[i];
       }
       return result;

        }
};