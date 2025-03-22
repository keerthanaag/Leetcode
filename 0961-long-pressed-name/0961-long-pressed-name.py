class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed):
            return False
        n=len(name)
        j=0
        for i,x in enumerate(typed):
            print(x)
            if j < len(name) and x == name[j]:
                print("if",name[j])
                j+=1
            elif j != 0 and x == name[j-1] :
                continue
            else:
                return False
        print(j)
        if j != len(name):
            return False
        return True

        