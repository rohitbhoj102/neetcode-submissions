class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # initiate result and a list, to be appended then joined
        res = []
        # create two pointers at the left of each word
        l1, l2 = 0, 0

        # while each pointer is still part of the word,
        while l1 < len(word1) or l2 < len(word2):
            if l1 < len(word1):
                # append from first word
                res.append(word1[l1])
                l1 += 1
            if l2 < len(word2):
                # then append from second word
                res.append(word2[l2])
                l2 += 1

        return "".join(res)
        

        

