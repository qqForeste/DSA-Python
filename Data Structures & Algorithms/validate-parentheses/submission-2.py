class Solution:
    def isValid(self, s: str) -> bool:
        
        d = {'[':']', '{':'}','(':')'}


        stack = []

        for c in s:
            if c in d:
                stack.append(c)
            elif stack and c == d[stack[-1]]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0