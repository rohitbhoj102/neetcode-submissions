class Solution:
    def isPalindrome(self, s: str) -> bool:
        # option 1: O(n) time, O(n) space
        # cleaned = [c.lower() for c in s if c.isalnum()]
        # return cleaned == cleaned[::-1]

        #option 2: two pointer -> O(1) space
        l, r = 0, len(s)-1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


        