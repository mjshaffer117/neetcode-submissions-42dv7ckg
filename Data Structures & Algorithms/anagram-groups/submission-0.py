class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            hashmap.setdefault("".join(sorted(s)), []).append(s)

        return list(hashmap.values())