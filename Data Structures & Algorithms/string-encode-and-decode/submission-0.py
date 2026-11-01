class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(str(len(s)))
            parts.append("#")
            parts.append(s)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # find the '#' terminating the length
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            res.append(s[i : i + length])
            i += length
        return res
