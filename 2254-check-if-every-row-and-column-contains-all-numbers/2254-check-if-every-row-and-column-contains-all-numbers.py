class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        temp = [1] * n  # Expected frequency array
        
        for i in range(n):
            arr_row = [0] * n  # Frequency array for row
            arr_col = [0] * n  # Frequency array for column

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

            print(f"Row {i}: {arr_row}, Expected: {temp}")
            print(f"Col {i}: {arr_col}, Expected: {temp}")
            
            if arr_row != temp or arr_col != temp:
                return False  # Early return if any row or column is invalid
        
        return True 