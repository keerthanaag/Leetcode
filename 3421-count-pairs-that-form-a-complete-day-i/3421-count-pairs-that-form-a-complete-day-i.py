class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        lst=[]
        for i in range(len(hours)):
            for j in range(i+1,len(hours)):
                check = (hours[i]+hours[j])//24
                print(check,(hours[i]+hours[j])%24)
                if (hours[i]+hours[j])%24==0:
                    val=(i,j)
                    lst.append(val)
        return len(lst)

        