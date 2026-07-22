class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr) - 1
        curr = arr[n]
        arr[n] = -1
        
        for i in range(n - 1, -1, -1):
            if arr[i] < curr:
                arr[i] = curr
            else:
                temp = arr[i]
                arr[i] = curr
                curr = temp

        return arr