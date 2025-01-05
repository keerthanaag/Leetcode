class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        shift_acc = [0] * (n + 1)
        for x in shifts:
            start, end, direction = x
            if direction == 0:  
                shift_acc[start] -= 1
                shift_acc[end + 1] += 1
            else:  
                shift_acc[start] += 1
                shift_acc[end + 1] -= 1

        net_shifts = [0] * n
        current_shift = 0
        for i in range(n):
            current_shift += shift_acc[i]
            net_shifts[i] = current_shift

        result = []
        for i, char in enumerate(s):
            shift = net_shifts[i] % 26 
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)

        return "".join(result)
        