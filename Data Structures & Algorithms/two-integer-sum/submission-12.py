class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        prevElem = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in prevElem:
                return [prevElem[diff],i]
            prevElem[num] = i
        