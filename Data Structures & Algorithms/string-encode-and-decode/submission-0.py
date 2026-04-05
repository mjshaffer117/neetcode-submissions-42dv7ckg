class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret = ret + str(len(s)) + '#' + s
        return ret

    def decode(self, s: str) -> List[str]:
        i, ret = 0, []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            n = int(s[i:j])
            i = j + 1
            j = i + n
            ret.append(s[i:j])
            i = j
        return ret