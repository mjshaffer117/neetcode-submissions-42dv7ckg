class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            cnts[n] = cnts.get(n, 0) + 1
        for n, c in cnts.items():
            freq[c].append(n)
        
        res = []
        for i in freq[::-1]:
            for j in i:
                if j is None:
                    continue
                res.append(j)
            if len(res) == k:
                return res
