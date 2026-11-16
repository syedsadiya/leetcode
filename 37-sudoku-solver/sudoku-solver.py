class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Initialize tracking sets and collect empty cells
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empty_cells.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def backtrack(index: int) -> bool:
            if index == len(empty_cells):
                return True

            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + (c // 3)

            for char_val in map(str, range(1, 10)):
                if (char_val not in rows[r] and 
                    char_val not in cols[c] and 
                    char_val not in boxes[box_idx]):
                    
                    # Place number
                    board[r][c] = char_val
                    rows[r].add(char_val)
                    cols[c].add(char_val)
                    boxes[box_idx].add(char_val)

                    if backtrack(index + 1):
                        return True

                    # Backtrack (remove number)
                    board[r][c] = '.'
                    rows[r].remove(char_val)
                    cols[c].remove(char_val)
                    boxes[box_idx].remove(char_val)

            return False

        backtrack(0)