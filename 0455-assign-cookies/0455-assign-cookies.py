class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count=0
        g=sorted(g)#sort them so they are in order
        s=sorted(s)
        for x in g:
            for y in s:
                if y>=x:
                    count+=1
                    s.remove(y)
                    break
        return count


        