class MySolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        schars, tchars = dict(), dict() # O(U) worst case all unique chars mem complexity 
        for i in range(len(s)): # O(N)
            if s[i] in schars:
                schars[s[i]] += 1
            else:
                schars[s[i]] = 1
            
            if t[i] in tchars:
                tchars[t[i]] += 1
            else:
                tchars[t[i]] = 1
        
        if tchars == schars: # O(N) average case
            return True
        return False

# fixed alphabet optimization: constained input space -> use fixed array
# balancing counts to ensure equallity in character counts

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26 # O(1) constant mem complexity
        # O(N)
        for i in s:
            record[ord(i) - ord("a")] += 1
        for i in t:
            record[ord(i) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                return False
        return True