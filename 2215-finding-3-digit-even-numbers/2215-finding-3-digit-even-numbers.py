from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]: 
        unique_numbers = set()  
        
        for num in permutations(digits, 3):  
            if num[0] != 0 and num[2] % 2 == 0:  
                unique_numbers.add(num[0] * 100 + num[1] * 10 + num[2])
        
        return sorted(unique_numbers)
        