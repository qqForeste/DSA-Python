#include <unordered_map>
#include <stack>

class Solution {
public:
    bool isValid(string s) {

        unordered_map<char,char> dict = {{'}', '{'}, {']', '['},{')','('}};
        stack<char> pstack{};

        for (char c : s)
        {   
            if (dict.contains(c))
            {
                if (!pstack.empty() && pstack.top() == dict[c])
                {
                    // stack = [[
                    pstack.pop();
                }
                else
                {
                    return false;
                }
            }
            else
            {
                pstack.push(c);
            }

        }

        return pstack.empty() == true;
    }
};
