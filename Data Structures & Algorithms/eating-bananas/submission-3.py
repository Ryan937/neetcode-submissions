class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        result = high

        while low <= high:
            mid = low + (high - low) // 2
            rate = sum(math.ceil(p / mid) for p in piles)
             
            if rate > h:
                low = mid + 1
            else:
                high = mid - 1
                result = mid
        
        return result

