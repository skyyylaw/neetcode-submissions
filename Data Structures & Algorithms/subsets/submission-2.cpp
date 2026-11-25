class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> output = {{}};
        for (auto n: nums){
            int size = output.size();
            for (int i = 0; i<size; i++){
                output.push_back(output[i]);
                output.back().push_back(n);
            }
        }
        return output;
    }
};
