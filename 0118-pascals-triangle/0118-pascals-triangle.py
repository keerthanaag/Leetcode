class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        for i in range(0,numRows):
            temp =[]
            for j in range(0,i+1):
                if i == j or j == 0:
                    temp.append(1)
                else:
                    val = pascal[i-1][j-1]+pascal[i-1][j]
                    temp.append(val) 
            pascal.append(temp)
        return pascal

