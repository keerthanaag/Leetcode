class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        add=sum(chalk)
        val=k%add
        print(val,add)
        for i,x in enumerate(chalk):
            if val<x:
                return i
            val-=x
        return -1
        
        