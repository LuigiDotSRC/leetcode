from typing import List
from collections import defaultdict

# hashsets for duplicate O(1) lookup
# mathematical mapping of 3x3 squares indices

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = defaultdict(set[int]), defaultdict(set[int]), defaultdict(set[int])
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]:
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
            
        return True


# initial attempt close to solution

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         rows, cols = defaultdict(set[int]), defaultdict(set[int])
#         for i in range(len(board)):
#             for j in range(len(board)):
#                 if board[i][j] in rows[i] or board[i][j] in cols[j]:
#                     return False
#                 rows[i].add(board[i][j])
#                 cols[j].add(board[i][j])