class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        base = ord('a')
        for s in strs:
            charmap = [0] * 26
            for c in s:
                i = ord(c) - base
                charmap[i] += 1
            key = tuple(charmap)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(s)
        return list(hashmap.values())
            