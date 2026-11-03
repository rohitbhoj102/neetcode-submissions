from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                box = (r // 3, c // 3)

                if (val in rows[r] or
                    val in cols[c] or
                    val in squares[box]):
                    return False

                rows[r].add(val)
                cols[c].add(val)
                squares[box].add(val)

        return True