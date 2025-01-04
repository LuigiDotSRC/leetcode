from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}?" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        acc = ""
        i = 0
        while i < len(s):
            if s[i] == '?':
                wl = int(acc)
                acc = ""
                for j in range(1, wl+1):
                    acc += s[i+j]
                res.append(acc)
                acc = ""
                i += wl + 1
            else:
                acc += s[i]
                i += 1

        return res
    
if __name__ == "__main__":
    sol = Solution()
    enc = sol.encode(["hello", "world"])
    dec = sol.decode(enc)
    print(enc, dec)