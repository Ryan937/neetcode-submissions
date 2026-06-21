class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = dict()

        for i in range(len(nums)):
            curr = nums[i]

            if target - curr in my_map:
                return [my_map[target - curr], i]
            else:
                my_map[curr] = i

        return None