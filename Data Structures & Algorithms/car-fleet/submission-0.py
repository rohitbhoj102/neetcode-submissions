from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # monotonic stack
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)  # front-most car first

        stack = []  # arrival times of distinct fleets
        for p, s in pair:
            time = (target - p) / s
            stack.append(time)
            # If this car catches the fleet ahead, merge into it
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)