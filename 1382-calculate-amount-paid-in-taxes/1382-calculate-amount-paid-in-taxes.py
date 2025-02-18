class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = 0
        prev = 0
        for i,x in enumerate(brackets):
            if income > prev:
                ans += (min(x[0], income)-prev )* (x[1] / 100)
                prev = x[0]
            else:
                break
        ans = round(ans, 5)
        return ans
        
        