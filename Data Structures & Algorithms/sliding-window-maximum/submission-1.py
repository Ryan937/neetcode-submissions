class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        i = 0
        j = k - 1

        while j < len(nums):
            curr = -999
            x = i

            while x <= j:
                curr = max(curr, nums[x])
                x += 1
            
            result.append(curr)
            i += 1
            j += 1

        return result