# same balancing principle used in 242-ValidAnagram

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0] * 26
        for c in s1:
            freq[ord(c) - ord('a')] += 1

        window = [0] * 26
        l = 0
        for r in range(len(s2)):
            window[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 == len(s1):
                if window == freq:
                    return True
                window[ord(s2[l]) - ord('a')] -= 1
                l += 1

        return False