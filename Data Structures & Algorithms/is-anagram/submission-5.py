class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s2 = [c.lower() for c in s if c.isalnum()]
        t2 = [c.lower() for c in t if c.isalnum()]

        if len(s2) != len(t2): return False

        counts = dict()

        for i in range(len(s2)):
            counts[s2[i]] = counts.get(s2[i], 0) + 1
            counts[t2[i]] = counts.get(t2[i], 0) - 1

        for i in counts.values():
            if i != 0:
                return False

        return True