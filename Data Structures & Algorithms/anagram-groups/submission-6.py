from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        d = defaultdict(list)
        res =[]

        for i in strs:
            sorted_i = tuple(sorted(i))
            d[sorted_i].append(i)

        for i in d.values():
            res.append(i)

        return res



        
        

