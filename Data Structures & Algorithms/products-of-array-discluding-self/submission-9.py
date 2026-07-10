class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1
        postfix = 1
        output = [1] * len(nums)

        for n in range(len(nums)):
            output[n] = prefix
            prefix *= nums[n]

        for n in range(len(nums)-1, -1, -1):
            output[n] *= postfix
            postfix *= nums[n]
        
        return output
        