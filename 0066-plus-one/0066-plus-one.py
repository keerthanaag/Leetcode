class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = 0
        for i in range(len(digits)-1,-1,-1):
            print(i,digits[i],"first")
            if flag == 1:
                if digits[i] < 9:
                    digits[i] = digits[i]+1
                    flag = 0
                    print("break 1")
                    break
                else:
                    digits[i] = 0
                    flag = 1
            #print(digits[i])
            else:
                if digits[i] < 9 :
                    digits[i] = digits[i]+1
                    print("break 2")
                    break
                else:
                    digits[i] = 0
                    flag = 1
        if flag == 1:
            digits.insert(0,1)
            print(i,digits[i],"last")
        print(digits)
        return digits
