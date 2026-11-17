class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Algorithm: Sliding Window (Dynamic Window Size)
        count = {}
        l = 0
        maxf = 0

        for r in range(len(s)):
            # add right character to window
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])

            # window is invalid - shrink from left
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return r - l + 1