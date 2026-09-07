#include <cctype>

class Solution {
public:
    bool isPalindrome(string s) {
        
        int left = 0;
        int right = s.size() - 1;

        while (left < right)
        {
            while ((left < right) && !isAlphanumeric(s[left]))
            {
                left += 1;
            }
            while ((left < right) && !isAlphanumeric(s[right]))
            {
                right -= 1;
            }

            if (tolower(s[left]) != tolower(s[right]))
            {
                return false;
            }

            left += 1;
            right -= 1;

        }

        return true;

    }

    bool isAlphanumeric(char c)
    {
        if (('a' <= c && c <= 'z') ||
            ('A') <= c && c <= ('Z') ||
            ('0') <= c && c <= ('9'))
            {
                return true;
            }
        else
        {
            return false;
        }
    }

};
