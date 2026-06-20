class Solution:
    def maxDifference(self, s: str) -> int:
        my_map = dict()

        for c in s:
            my_map[c] = my_map.get(c, 0) + 1
        
        odd = float("-inf")
        even = float("inf")

        for val in my_map.values():
            if val % 2 == 0:
                even = min(even, val)
            else:
                odd = max(odd, val)

        return odd - even