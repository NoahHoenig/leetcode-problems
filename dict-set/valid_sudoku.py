class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        #Checks rows
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[i])):
                if board[i][j] != "." and board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])
        #Checks columns
        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[j][i] != "." and board[j][i] in seen:
                    return False
                else:
                    seen.add(board[j][i])
        #Check boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        if board[row + i][col + j] != "." and board[row + i][col + j] in seen:
                            return False
                        else: 
                            seen.add(board[row + i][col + j])

        return True
s = Solution()
print(s.isValidSudoku([["5","3",".",".","7",".",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]))     