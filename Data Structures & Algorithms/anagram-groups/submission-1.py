class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        base = ord('a')
        for s in strs:
            charmap = [0] * 26
            for c in s:
                i = ord(c) - base
                charmap[i] += 1
            hashmap[tuple(charmap)].append(s)
        return list(hashmap.values())
            