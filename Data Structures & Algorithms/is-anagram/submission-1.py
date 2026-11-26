class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Frequency counting (hashmap)
        if len(s) != len (t):
            return False

        hashs, hasht = {}, {}

        for ch in s:
            hashs[ch] = hashs.get(ch, 0) + 1
        
        for ch in t:
            hasht[ch] = hasht.get(ch, 0) + 1

        return hasht == hashs
            

        