#include<unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> numdict;
        vector<int> res = {};

        for (int i = 0; i < nums.size(); i++){
            int compliment = target - nums[i];
            if (numdict.contains(compliment))
            {
                if (i < numdict[compliment])
                {
                    res.push_back(i);
                    res.push_back(numdict[compliment]);
                }
                else
                {
                    res.push_back(numdict[compliment]);    
                    res.push_back(i);
                }
                return res; 
            }
            numdict[nums[i]] = i; 
        }

        return res;
    }
};
