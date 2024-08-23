class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=1
        j=0
        lst=[]
        while len(lst)<=k:
            if j < len(arr) and i == arr[j]:
                j+=1
            else:
                lst.append(i)
            i+=1
        return lst[k-1]
        