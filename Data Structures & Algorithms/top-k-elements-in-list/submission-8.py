class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        prev = {}
        freq = [[] for i in range(len(nums)+1)]
        res = []


        for n in nums:
            prev[n] = 1 + prev.get(n,0)

        for n,c in prev.items():
            freq[c].append(n)

        for i in range(len(freq)-1, 0 ,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        