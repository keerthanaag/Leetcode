class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lst=[]
        row=[]
        col=[]
        #row wise minimum
        for i in range(len(matrix)):
            row_min=min(matrix[i])
            row.append(row_min)
        #col wise maximum
        for j in range(len(matrix[i])):
            tempc=[]
            for val in matrix:
                tempc.append(val[j])
            j+=1
            col_max=max(tempc)
            #print(tempc,col_max)
            col.append(col_max)
        ans=list(set(row).intersection(set(col)))
        return ans
                
                