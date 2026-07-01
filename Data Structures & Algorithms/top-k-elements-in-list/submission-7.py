class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        freq = [[] for i in range(len(nums)+1)]
        res = []
        d= {}

        for i in nums:
            d[i] = 1 + d.get(i,0)
        for n,c in d.items():
            freq[c].append(n)

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res




        
        