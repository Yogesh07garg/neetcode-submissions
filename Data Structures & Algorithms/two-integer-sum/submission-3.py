class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevElem = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevElem:
                return [prevElem[diff],i]

            prevElem[n] = i
