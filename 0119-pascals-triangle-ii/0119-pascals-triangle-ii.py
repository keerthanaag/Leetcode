class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lst=[]
        temp=[]
        numRows=rowIndex+1
        for i in range(1,numRows+1):
            for j in range(i):
                if j == 0 or j == i-1:
                    temp.append(1)
                else:
                    temp.append(lst[-1][j-1]+lst[-1][j])
            lst.append(temp)
            temp=[]
        return lst[rowIndex]
        