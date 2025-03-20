class Solution:
    def maxDifference(self, s: str) -> int:
        d = {}
        for x in s:
            if x in d:
                val = d[x] + 1
            else:
                val = 1
            d.update({x:val})
        fl_odd = 0
        fl_even = 0
        for x in d:
            if d[x] %2 != 0:
                if fl_odd == 0:
                    odd = d[x]
                    fl_odd = 1
                else:
                    odd = max(odd,d[x])
            if d[x] %2 == 0:
                if fl_even == 0:
                    even = d[x]
                    fl_even = 1
                else:
                    even = min(even,d[x])  
        return odd-even 