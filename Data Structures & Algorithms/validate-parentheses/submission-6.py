class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        d = {'[':']', '(':')', '{':'}'}

        """"
            stack: [

            []


        """

        for bracket in s:
            if not bracket in d:
                if stack and bracket == d[stack[-1]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
            print("bracket: ", bracket)
            print("current stack:" , stack)
        
        return len(stack) == 0