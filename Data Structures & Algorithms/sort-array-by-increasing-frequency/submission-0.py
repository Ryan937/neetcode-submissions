class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        
        for num in nums:
            freq[num] += 1
        
        nums.sort(key=lambda x: (freq[x], -x))
        return nums