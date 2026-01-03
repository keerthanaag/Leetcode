class Solution:
    def pivotInteger(self, n: int) -> int:
        numbers = list(range(1, n + 1))
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2

            left_sum = sum(numbers[:mid])        # 1 to mid
            right_sum = sum(numbers[mid-1:])     # mid to n

            print(left, right, mid, left_sum, right_sum)

            if left_sum == right_sum:
                return mid
            elif left_sum < right_sum:
                left = mid + 1
            else:
                right = mid - 1

        return -1