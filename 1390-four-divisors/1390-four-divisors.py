import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        
        for n in nums:
            divisors = set()
            
            for d in range(1, int(math.sqrt(n)) + 1):
                if n % d == 0:
                    divisors.add(d)
                    divisors.add(n // d)
                    
                if len(divisors) > 4:
                    break
            
            if len(divisors) == 4:
                total += sum(divisors)
        
        return total
        