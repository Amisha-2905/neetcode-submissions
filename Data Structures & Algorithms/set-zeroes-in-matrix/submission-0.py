class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        stackM = [1] * m
        stackN =  [1] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    stackM[i] = 0
                    stackN[j] = 0
        for i in range(m):
            if stackM[i] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n):
            if stackN[j] == 0:
                for i in range(m):
                    matrix[i][j] = 0        