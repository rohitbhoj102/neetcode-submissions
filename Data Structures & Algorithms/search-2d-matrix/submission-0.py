class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1

        while low <= high:
            mid = (low + high) // 2
            val = matrix[mid // cols][mid % cols]
            if target > val:
                low = mid + 1
            elif target < val:
                high = mid - 1
            else:
                return True
        return False
