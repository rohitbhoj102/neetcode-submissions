from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap to store each anagram 
        # key --> anagram, value --> list of anagrams
        # for each str in strs, 
        # if the str is in the hashmap, add into the list for that respective key
        # else create new key value pair
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)

        return list(ans.values())
        