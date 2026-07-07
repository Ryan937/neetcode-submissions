class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            s1 = max(stones)
            stones.remove(s1)
            s2 = max(stones)
            stones.remove(s2)

            if s1 != s2:
                stones.append(s1 - s2)

        return stones[0] if len(stones) == 1 else 0