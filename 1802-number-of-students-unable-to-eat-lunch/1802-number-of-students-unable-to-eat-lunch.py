from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        d=deque()
        d.extend(students)
        while(1):
            flag=0
            i=0
            while i < len(students):
                if students[0] == sandwiches[0]:
                    flag=1
                    students.pop(0)
                    sandwiches.pop(0)
                else:
                    students.append(students.pop(0))
                i+=1
            if flag==0:
                break
        return len(students)
            
                