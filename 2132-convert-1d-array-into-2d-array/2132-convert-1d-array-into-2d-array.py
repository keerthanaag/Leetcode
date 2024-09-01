class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        lst=[]
        temp=[]
        if m*n != len(original):
            return []
        i=0
        while i <len(original):
            temp.append(original[i])
            i+=1
            if len(temp)==n:
                lst.append(temp)
                temp=[]
        return lst
            
        