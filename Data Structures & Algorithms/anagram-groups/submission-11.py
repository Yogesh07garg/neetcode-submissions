from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        Elem = defaultdict(list)

        for s in strs:
            sorted_s = tuple(sorted(s))
            Elem[sorted_s].append(s)
        for val in Elem.values():
            res.append(val)
        return res

     
        