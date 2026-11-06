class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Algorithm Family: Monotonic Stack
        res = [0] * len(temperatures)
        stack = [] # holds (temp, index), pairs, decreasing temps

        for i, t in enumerate(temperatures):
            # current day is warmer than days sitting on top of the stack
            while stack and t > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                res[stack_index] = i - stack_index
            stack.append((t, i))

        return res

