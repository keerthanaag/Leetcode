class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        d={}
        for x in pick:
            if str(x) not in d:
                val=1
            else:
                val=d[str(x)]+1
            d.update({str(x):val})
        print(d)
        st=set({})
        for x in d.keys():
            if int(x[1])<d[x]:
                print(x,d[x])
                st.add(int(x[1]))
        return len(st)
        