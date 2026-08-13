class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):

            while stack and stack[-1][0] < temperatures[i]:
                stackTemp, stackIndex = stack.pop()
                print(res)
                print(stackIndex)
                res[stackIndex] = i - stackIndex
            
            stack.append([t, i])
        
        return res