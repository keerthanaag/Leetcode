class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst=[]
        temp=[]
        for i in range(1,numRows+1):
            for j in range(i):
                if j == 0 or j == i-1:
                    temp.append(1)
                else:
                    temp.append(lst[-1][j-1]+lst[-1][j])
            lst.append(temp)
            temp=[]
        return lst

        