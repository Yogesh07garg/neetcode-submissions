from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        prev = defaultdict(list)
        res = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            prev[sorted_s].append(s)

        for val in prev.values():
            res.append(val)

        return res


        