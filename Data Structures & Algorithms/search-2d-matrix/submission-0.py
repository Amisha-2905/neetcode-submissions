class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        row = -1

        while l <= r:
            mid = (l + r) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1

        if row == -1:
            return False

        l = 0
        r = len(matrix[row]) - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                r = mid - 1

        return False