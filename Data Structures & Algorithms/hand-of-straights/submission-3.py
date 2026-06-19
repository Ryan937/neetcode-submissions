class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        
        counts = dict()

        for i in hand:
            counts[i] = counts.get(i, 0) + 1

        counts = dict(sorted(counts.items()))
        lowest = min(counts)

        for num in hand:
            if counts[num] == 0:
                continue

            for i in range(groupSize):
                curr = num + i

                if counts.get(curr, 0) == 0:
                    return False
                
                counts[curr] -= 1

        return True

