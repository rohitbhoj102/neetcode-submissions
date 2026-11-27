class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # algo: horizontal scanning (prefix)
        prefix = strs[0] # take the first word as prefix

        # loop through all other words
        for word in strs[1:]:
            # shrink prefix until it is a prefix of the word
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix