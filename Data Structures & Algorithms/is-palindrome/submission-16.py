class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1

        while left < right:
            
            while left < right and not self.alphaNum(s[left]):
                left += 1
            
            while left < right and not self.alphaNum(s[right]):
                right -= 1

            print(left, right)

            if s[left].lower() != s[right].lower():
                return False

            left, right = left + 1, right - 1

        return True

    

    def alphaNum(self, c):
        return (ord('0') <= ord(c) <= ord('9') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z')       
        )