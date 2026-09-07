#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
        {
            return false;
        }
        
        unordered_map<int,int> sdict;
        unordered_map<int,int> tdict;

        for (int i = 0; i < s.size(); i++)
        {
            int count = s[i] - 'a';
            sdict[count] += 1;
            int count2 = t[i] - 'a';
            tdict[count2] +=1;
        }

        return (sdict == tdict);
                
    }
};
