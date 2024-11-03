class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # place=s.find(goal[0])
        # if place == -1:
        #     return False
        # else:
        #     temp = s[place:]+s[:place]
        #     print("temp",temp)
        #     if temp == goal:
        #         return True
        #     else:
        #         return False
        place=s.find(goal[0])
        if s == goal:
            return True
        elif place == -1:
            return False
        else:
            temp = s[place:]+s[:place]
            print("temp",temp)
            if temp == goal:
                return True
            else:
                for i in range(place+1,len(s)):
                    if s[i]==goal[0]:
                        place=i
                        temp = s[place:]+s[:place]
                        print("temp",temp)
                        if temp == goal:
                            return True
                return False
