class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        print(seats,students)
        pos = 0
        for i in range(len(seats)):
            pos += abs(seats[i]-students[i])
        return pos
        