class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
       # Algorithm: Monotonic Stack
       max_area = 0
       stack = []
       
       for i, h in enumerate(heights):
        start = i
        # current bar is shorter -> pop taller bars and finalise them 
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index # inherit the earlier start
        stack.append((start, h))
    
       # remaining bars extend to the end of the array
       for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))

       return max_area

        