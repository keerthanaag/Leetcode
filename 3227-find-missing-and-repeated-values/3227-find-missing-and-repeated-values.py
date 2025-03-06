class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        import numpy as np
        # lst=[]
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         lst.append(grid[i][j])
        # for i in range(1,len(lst)+1):
        #     if i not in lst:
        #         miss=i
        #     if lst.count(i)==2:
        #         count=i
        # ans=[count,miss]
        # return ans
        a=np.array(grid)
        a=a.flatten()
        temp=sorted(a)
        print(temp)
        lst=[i+1 for i in range(len(temp))]
        miss=list(set(lst)-set(temp))
        for i in range(len(temp)):
            if temp.count(lst[i]) >1:
                count=lst[i]
                break
        return [count,miss[0]]
        