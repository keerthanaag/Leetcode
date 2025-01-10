class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        lst = []
        decimal = 0  # Initialize the decimal representation
        for num in nums:
            # Update the decimal representation iteratively
            decimal = (decimal * 2 + num) % 5  # Keep only the remainder
            lst.append(decimal == 0)  # Check divisibility by 5
        return lst

        