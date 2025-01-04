class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = []
        flag =0
        if k < 0:
            code = code[::-1]
            k = abs(k)
            flag = 1
        for i in range(0,len(code)):
            if k != 0:
                print(code)
                if len(code) > (i+k+1):
                    ans.append(sum(code[i+1:i+k+1]))
                else:
                    f = sum(code[i+1:len(code)])
                    temp = k - (len(code)-(i+1))
                    val = f + sum(code[0:temp])
                    ans.append(val)
            else:
                ans.append(0)
        if flag == 1:
            return ans[::-1]
        return ans