class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_map = {}
        t_map = {}

        for i in range(len(s)):
            cs = s[i]
            ct = t[i]

            if cs not in s_map and ct not in t_map:
                s_map[cs] = i
                t_map[ct] = i
            elif cs not in s_map and ct in t_map or cs in s_map and ct not in t_map or s_map[cs] != t_map[ct]:
                return False

        return True