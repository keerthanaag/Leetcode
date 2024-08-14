class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum_single_digit=0
        sum_double_digit=0
        for x in nums:
            if x <10:
                sum_single_digit+=x
            else:
                sum_double_digit+=x
        if sum_single_digit != sum_double_digit:
            return True
        return False
        