class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()

        for curr_val, next_val in zip(nums, nums[1:]):
            if curr_val == next_val:
                return curr_val
        
        return -1