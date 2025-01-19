from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        n = rows * cols - 1 

        def bs(start, end):
            if start > end:
                return False
            mid = start + (end - start) // 2  
            curr = matrix[mid // cols][mid % cols]

            if curr == target:
                return True
            elif curr > target:
                return bs(start, mid - 1)
            else:
                return bs(mid + 1, end)

        return bs(0, n)
