# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs

        mid = len(pairs) // 2
        left = self.mergeSort(pairs[:mid])
        right = self.mergeSort(pairs[mid:])

        return self.merge(left, right)

    def merge(self, left_half, right_half):
        i = j = 0
        sorted_list = []

        while i < len(left_half) and j < len(right_half):
            if left_half[i].key <= right_half[j].key:
                sorted_list.append(left_half[i])
                i += 1
            elif left_half[i].key > right_half[j].key:
                sorted_list.append(right_half[j])
                j += 1

        sorted_list.extend(left_half[i:])
        sorted_list.extend(right_half[j:])
        return sorted_list