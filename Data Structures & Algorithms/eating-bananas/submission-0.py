class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = l + (r - l) // 2 # safe division (avoid overflow)
            t = 0
            for p in piles:
                t += (p + k - 1) // k
            if t <= h:
                res = k # new lowest value
                r = k - 1
            else: # t > h
                l = k + 1
        return res