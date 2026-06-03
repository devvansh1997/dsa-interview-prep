class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        start, end = 0, ROWS - 1
        while start <= end:
            row = (start + end) // 2
            if target > matrix[row][-1]:
                start = row + 1
            elif target < matrix[row][0]:
                end = row - 1
            else:
                break
        
        if not (start <= end):
            return False
        else:
            l, r = 0, len(matrix[row])-1
            while l <= r:
                mid = (l + r) // 2
                if target > matrix[row][mid]:
                    l = mid + 1
                elif target < matrix[row][mid]:
                    r = mid - 1
                else:
                    return True
        return False