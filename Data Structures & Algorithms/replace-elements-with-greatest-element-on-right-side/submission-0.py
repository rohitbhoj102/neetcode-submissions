class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        n = len(arr)
        for i in range(n-1, -1, -1):
            original = arr[i]
            arr[i] = rightMax
            rightMax = max(original, rightMax)
        return arr
