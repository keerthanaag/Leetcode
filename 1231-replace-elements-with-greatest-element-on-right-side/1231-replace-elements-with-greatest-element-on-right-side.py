class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr.reverse()
        lst=[]
        maxval=0
        lst.append(-1)
        for i in range(1,len(arr)):
            if maxval<arr[i-1]:
                maxval=arr[i-1]
            lst.append(maxval)
        print(lst)
        lst.reverse()       
        return lst