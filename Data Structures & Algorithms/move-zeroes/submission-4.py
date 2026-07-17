class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, j = 0, 0

        while j < len(nums):
            if nums[j] != 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1

            j += 1