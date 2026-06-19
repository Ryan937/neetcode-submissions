class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        total = m + n
        i = 0

        while m < total:
            nums1[m] = nums2[i]
            m += 1
            i += 1
        
        return nums1.sort()