class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    row_val = (i, num)
                    col_val = (num, j)
                    box_val = (i // 3, j // 3, num)
                    
                    if row_val in seen or col_val in seen or box_val in seen:
                        return False
                    
                    seen.add(row_val)
                    seen.add(col_val)
                    seen.add(box_val)
                    
        return True