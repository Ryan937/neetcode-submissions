class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        curr = 0

        for i in nums:
            if i != curr:
                return curr

            curr += 1

        return len(nums)