# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) -1)
        return pairs

    def quickSortHelper(self, arr: List[Pair], s: int, e: int) -> None:
        # base case: subarray with 0 or 1 elements
        if e - s + 1 <= 1:
            return

        pivot = arr[e]  # Right-most element
        left = s  # Pointer for the boundary of smaller elements

        # Partition: move all smaller elements to the left side
        for i in range(s, e):
            if arr[i].key < pivot.key:
                # Swap current element with position at 'left'
                arr[left], arr[i] = arr[i], arr[left]
                left += 1
        
        # Place pivot in its correct position
        arr[e], arr[left] = arr[left], arr[e]
        
        # Recursively sort left and right partitions
        self.quickSortHelper(arr, s, left - 1)
        self.quickSortHelper(arr, left + 1, e)
