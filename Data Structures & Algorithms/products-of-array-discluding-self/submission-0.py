class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        for i in range(n):
            p = 1
            for j in range(n):
                if i == j:
                    continue
                else:
                    p *= nums[j]
            output[i] = p
        return output
