class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for index, value in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][1] < value:
                result[stack[-1][0]] = index - stack[-1][0]
                stack.pop()
            stack.append([index, value])
        for i in range(len(stack)):
            result[stack[i][0]] = 0

        return result

