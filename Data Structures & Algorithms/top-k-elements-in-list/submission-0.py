class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:



        dict = {}
        freq = [[] for i in range(len(nums)+1) ]

        res = []

        for n in nums:
            dict[n] = 1 + dict.get(n,0)

        for i,num in dict.items():
            freq[num].append(i)

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res    
        