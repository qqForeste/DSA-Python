#include <array>

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
        {
            return false;
        }

        array<int, 26> sdict;
        array<int, 26> tdict;


        for (int i; i < s.size(); i++)
        {
            sdict[s[i] - 'a'] += 1;
            tdict[t[i] - 'a'] += 1;
        }
        
        for (int ch : sdict)
        {
            cout << ch << ' ';
        }
        cout << '\n';

        for (int ch1 : tdict)
        {
            cout << ch1 << ' ';
        }
        cout << '\n';




        return sdict == tdict;

    }
};
