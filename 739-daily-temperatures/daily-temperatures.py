class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        stack = []
        result = [0]*l
        for i in range(0, len(temperatures)):
            while(len(stack) != 0 and temperatures[stack[-1]] < temperatures[i]):
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return result