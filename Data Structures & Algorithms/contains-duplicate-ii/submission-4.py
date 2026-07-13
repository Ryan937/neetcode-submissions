class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or k <= 0: return False

        seen = set()
        i = j = 0

        while j < len(nums):
            if j - i > k:
                seen.remove(nums[i])
                i += 1
                seen.add(nums[i])
            
            if nums[j] not in seen:
                seen.add(nums[j])
            else:
                return True
            
            j += 1

        return False