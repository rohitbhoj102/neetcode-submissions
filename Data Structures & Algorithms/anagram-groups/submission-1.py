from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap to store each anagram 
        # key --> anagram, value --> list of anagrams
        # for each str in strs, sort them
        # if the str is in the hashmap, add into the list for that respective key
        # else create new key value pair
        ans = {}
        
        for s in strs:
            key = tuple(sorted(s))
            ans[key] = ans.get(key, []) + [s]
        return list(ans.values())