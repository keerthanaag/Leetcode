class Solution:
    def clearDigits(self, s: str) -> str:
        i=0
        while i< len(s):
            print(i)
            flag =0
            if s[i].isdigit():
                s = s[:i]+s[i+1:]
                print(s)
                flag = 1
                if i != 0 and s[i-1].isalpha():
                    s = s[:i-1]+s[i:]
                    print(f"entered second if {s}")
                elif i+1 < len(s) and s[i+1].isalpha():
                    s = s[:i+1]+s[i+2:]
                    print(f"entered elif {s}")
            if flag ==0 :
                i = i+1
            else:
                i=0 
        return s

        