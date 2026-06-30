class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = j = 0

        while j < len(nums):
            if nums[j] % 2 == 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
            
            j += 1

        return nums