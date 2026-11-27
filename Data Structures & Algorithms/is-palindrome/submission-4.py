class Solution:
    def isPalindrome(self, s: str) -> bool:
        # option 1: O(n) time, O(n) space
        # cleaned = [c.lower() for c in s if c.isalnum()]
        # return cleaned == cleaned[::-1]

        #option 2: two pointer -> O(1) space
        l, r = 0, len(s) - 1

        while l < r:
            # Skip non-alphanumeric characters from the left
            while l < r and not s[l].isalnum():
                l += 1
            # Skip non-alphanumeric characters from the right
            while l < r and not s[r].isalnum():
                r -= 1
            # Compare the two alphanumeric characters (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False
            # Move both pointers inward
            l += 1
            r -= 1

        return True

        