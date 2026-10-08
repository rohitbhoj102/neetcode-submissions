class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for val in operations:
            if val == '+':
                ## sum of two previous records
                scores.append(scores[-1] + scores[-2])
            elif val == 'D':
                ## double of previous score
                scores.append(scores[-1] * 2)
            elif val == 'C':
                ## remove from scores array
                scores.pop()
            else:
                scores.append(int(val))

        return sum(scores)
        