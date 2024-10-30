class Solution:
    def convertDateToBinary(self, date: str) -> str:
        s=date.split('-')
        num=''
        for x in s :
            num = num + str(bin(int(x)))[2:] + '-'
        return num[:-1]

        