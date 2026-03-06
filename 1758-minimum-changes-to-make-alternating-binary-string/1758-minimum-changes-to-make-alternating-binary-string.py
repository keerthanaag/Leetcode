class Solution:
    def countofoperations(self, s: str, start: int) -> int:
        cnt = 0
        for i in range(0,len(s)):
            if i %2 == 0:
                if int(s[i]) != start:
                    cnt += 1
            else:
                if int(s[i]) != (1-start):
                    cnt += 1
        print(start,cnt)
        return cnt
    def minOperations(self, s: str) -> int:
        return min(self.countofoperations(s,0),self.countofoperations(s,1))

        