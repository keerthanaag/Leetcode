class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        lst = []
        for i in range(len(score)):
            print(score[i])
            temp = [score[i][k],i]
            lst.append(temp)
        lst.sort(reverse=True)
        print(lst)
        new = []
        for i in range(len(lst)):
            new.append(score[lst[i][1]])
        print(score)
        return new
                