# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        for i in range(len(pairs)):
            l = i - 1
            while l >= 0 and pairs[l].key > pairs[l + 1].key:
                tmp = pairs[l]
                pairs[l] = pairs[l + 1]
                pairs[l + 1] = tmp
                l -= 1
            res.append(pairs.copy())
        return res
