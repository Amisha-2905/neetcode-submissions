class Solution:
    def checkrow(self, row: List[str]) -> bool:
        nums = [x for x in row if x != "."]
        return len(nums) == len(set(nums))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.checkrow(row):
                print(row)
                return False

        for i in range(9):
            column = [row[i] for row in board]
            if not self.checkrow(column):
                print(column)
                return False
        
        for i in range(3):
            for j in range(3):
                cell = []
                for k in range(3):
                    for l in range(3):
                        cell.append(board[i*3+k][j*3+l])
                if not self.checkrow(cell):
                    print(cell)
                    return False
        return True
           
        