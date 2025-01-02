class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        print(seats,students)
        pos = 0
        for i in range(len(seats)):
            pos += abs(seats[i]-students[i])
        return pos
        