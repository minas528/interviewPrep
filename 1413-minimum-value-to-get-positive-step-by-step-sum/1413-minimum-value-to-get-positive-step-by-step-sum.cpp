class Solution {
public:
    int minStartValue(vector<int>& nums) {
        vector<int> pre ;
        int acc = 0;
        // pre.push_back(9);
        for (int i =0 ;i<nums.size(); i++){
            acc += nums[i];
            pre.push_back(acc);
        }
        auto min = *min_element(pre.begin(), pre.end());
        if (min >0){
            return 1;
        }
        // cout<< "\nMin Element = "<<min;
        return min*-1 +1;
        
    }
};