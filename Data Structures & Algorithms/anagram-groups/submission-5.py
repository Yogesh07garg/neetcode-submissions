from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = defaultdict(list)
        res = []
        for s in strs:
            sorted_s = tuple(sorted(s))
            d[sorted_s].append(s)

        for val in d.values():
            res.append(val)
            
        return res
        

