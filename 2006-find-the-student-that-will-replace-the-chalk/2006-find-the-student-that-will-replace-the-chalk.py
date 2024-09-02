class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        add=sum(chalk)
        val=k%add
        print(val,add)
        for i,x in enumerate(chalk):
            if val<x:
                return i
            val-=x
        return -1
        