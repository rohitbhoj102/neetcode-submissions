class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # shrink window until duplicate is removed
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1 

            # add current character and update max
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len