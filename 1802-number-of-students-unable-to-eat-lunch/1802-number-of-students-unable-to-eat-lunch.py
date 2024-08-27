class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
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
        