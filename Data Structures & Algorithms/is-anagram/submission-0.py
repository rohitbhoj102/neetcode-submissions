class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashs = {}
        hasht = {}

        for ch in s:
            if ch in hashs:
                hashs[ch] += 1 
            else:
                hashs[ch] = 1

        for ch in t:
            if ch in hasht:
                hasht[ch] += 1
            else:
                hasht[ch] = 1
        
        return hashs == hasht