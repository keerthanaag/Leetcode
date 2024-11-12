class Solution:
    def minimumChairs(self, s: str) -> int:
        no_chairs = 1
        empty_chair = 1
        for x in s:
            if x == 'E':
                if empty_chair == 0:
                    no_chairs +=1
                    empty_chair +=1
                empty_chair -=1
            else:
                empty_chair +=1
        return no_chairs
        