class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        for i in range(0,numRows):
            temp =[]
            for j in range(0,i+1):
                if i == j or j == 0:
                    temp.append(1)
                else:
                    #2,1 = (1,0)+(1,1)
                    #3,1 = (2,0)+(2,1)
                    #3,2 = (2,1)+(2,2)
                    print(i,j)
                    val = pascal[i-1][j-1]+pascal[i-1][j]
                    temp.append(val) 
                print("temp",i,temp)
            pascal.append(temp)
            print("pascal",pascal)
        return pascal

