class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        pfx = sfx = 1
        for i in range(n):
            output[i] *= pfx
            pfx *= nums[i]
            j = n - i - 1
            output[j] *= sfx
            sfx *= nums[j]
        return output
