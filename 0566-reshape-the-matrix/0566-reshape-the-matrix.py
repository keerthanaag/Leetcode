import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        arr = np.array(mat)
        m,n = arr.shape
        if m*n != r*c:
            return mat
        return arr.reshape((r, c)).tolist()



        