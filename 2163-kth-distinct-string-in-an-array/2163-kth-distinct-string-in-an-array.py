class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        lst=[]
        #passed only 44 testcases
        #dup=[] 
        # for i,x in enumerate(arr):
        #     print(x,arr[i+1:],arr[:i])
        #     if x in arr[i+1:] or x in arr[:i]:
        #         if x not in dup:
        #             dup.append(x)
        #     else:
        #         lst.append(x)
        # print(lst,dup)
        # if len(lst)<k:
        #     return ""
        # else:
        #     return lst[k-1]
        d={}
        for x in arr:
            if x in d:
                val=d[x]
                val+=1
                d.update({x:val})
            else:
                d.update({x:1})
        for x in arr:
            if d[x]==1:
                lst.append(x)
        if len(lst)<k:
            return ""
        else:
            return lst[k-1]

        