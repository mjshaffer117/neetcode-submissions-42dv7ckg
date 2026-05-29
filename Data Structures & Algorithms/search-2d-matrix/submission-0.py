class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, btm = 0, len(matrix) - 1
        while top <= btm:
            mid = (top + btm) // 2
            row = matrix[mid]
            l, r = 0, len(row) - 1
            while row[l] <= target and row[r] >= target and l <= r:
                m = (l + r) // 2
                if row[m] == target:
                    return True
                elif row[l] < target:
                    l = m + 1
                else: # row[r] > target
                    r = m - 1
            if matrix[top][r] < target:
                top = mid + 1
            elif matrix[btm][l] > target:
                btm = mid - 1
        return False
                