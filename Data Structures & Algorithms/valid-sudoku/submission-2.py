class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        if rows != 9 or cols != 9:
            return False

        # Check rows
        for fullRow in board:
            seen = set()
            for char in fullRow:
                if char == ".":
                    continue
                if char in seen:
                    return False
                seen.add(char)

        # Check cols
        for fullCol in zip(*board):
            seen = set()
            for char in fullCol:
                if char == ".":
                    continue
                if char in seen:
                    return False
                seen.add(char)

        # Check nines
        for r in range(0,9,3):
            for c in range(0,9,3):
                seen = set()
                for dr in range(3):
                    for dc in range(3):
                        char = board[r+dr][c+dc]
                        if char == ".":
                            continue
                        if char in seen:
                            return False
                        seen.add(char)

        return True
