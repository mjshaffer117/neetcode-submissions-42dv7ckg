class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_nums = nums.copy()
        for n in nums:
            new_nums.append(n)
        return new_nums