class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const map = new Map<number, number>();

        for (let i = 0; i < nums.length; i++) {
            const curr = target - nums[i];

            if (map.has(curr))
                return [map.get(curr), i];
            else
                map.set(nums[i], i);
        }

        return null;
    }
}
