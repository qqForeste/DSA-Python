#include <array>
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
        {
            return false;
        }

        array<int, 26> sdict{};
        array<int, 26> tdict{};

        for (int i = 0; i < s.size(); i++)
        {
            sdict[s[i] - 'a'] += 1;
            tdict[t[i] - 'a'] += 1;
        }

        return (sdict == tdict);
    }
};
