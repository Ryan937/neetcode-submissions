class Solution:
    def maxDifference(self, s: str) -> int:
        my_map = dict()

        for c in s:
            my_map[c] = my_map.get(c, 0) + 1
        
        values = my_map.values()

        odds = [val for val in values if val % 2 == 1]
        evens = [val for val in values if val % 2 == 0]

        return max(odds) - min(evens)