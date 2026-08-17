class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest_yet = arr[-1]
        arr[-1] = -1
        n = len(arr)
        for i in range(n - 2, -1, -1):
            temp = arr[i]
            arr[i] = largest_yet
            largest_yet = max(largest_yet, temp)
        return arr