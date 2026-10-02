class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = []
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
        temp = hashmap.copy()
        while len(result) < k and temp:
            higher = max(temp, key=temp.get)
            result.append(higher)
            temp.pop(higher)
        return result