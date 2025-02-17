class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        temp = [1] * n 
        for i in range(n):
            arr_row = [0] * n  
            arr_col = [0] * n  
            for j in range(n):
                # Row check
                val_row = matrix[i][j]
                if val_row == 0 or val_row > n:
                    return False
                arr_row[val_row - 1] += 1                
                # Column check
                val_col = matrix[j][i]
                if val_col == 0 or val_col > n:
                    return False
                arr_col[val_col - 1] += 1
            
            if arr_row != temp or arr_col != temp:
                return False  
        
        return True 