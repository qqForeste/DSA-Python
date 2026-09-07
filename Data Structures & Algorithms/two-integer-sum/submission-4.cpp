#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numdict{};

        for (int i = 0; i < nums.size(); i++){
            int complement = target - nums[i];
            if (numdict.contains(complement))
            {
                return {numdict[complement], i};
            }

            numdict.insert({nums[i], i});
            }

        return {};
    }
};
