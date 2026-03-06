class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        i = 0
        flag = 0
        cnt = 0
        while i < len(mat):
            #print(i)
            #print(mat[i]) 
            if sum(mat[i]) > 1:
                i+= 1
                continue
            temp = []
            if mat[i][flag] == 1:
                for j in range(0,len(mat)):
                    temp.append(mat[j][flag])
                    if sum(temp)> 1:
                        continue
                    #print(mat[j][flag])
                #print(f" i: {i} : {mat[i]},j: {temp},{mat[i][flag]}")
                if sum(temp) == 1:
                    #print(f"The work i: {i} : {mat[i]},j: {temp},{mat[i][flag]}")
                    cnt += 1
            flag += 1
            #print(f"flag: {flag}")
            if flag == len(mat[i]):
                i += 1
                flag = 0
                #print(f"flag: {flag}")
        return cnt
        