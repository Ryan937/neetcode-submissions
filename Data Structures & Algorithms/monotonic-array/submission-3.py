class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = 0

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                if increasing == 0 or increasing == 1:
                    increasing = 1
                else:
                    return False
            
            if nums[i] > nums[i + 1]:
                if increasing == 0 or increasing == -1:
                    increasing = -1
                else:
                    return False

        return True