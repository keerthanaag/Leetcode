class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer=[]
        for i in range(0,n):
            temp=i+1
            if temp%3==0 and temp%5==0:
                answer.append("FizzBuzz")
            elif temp%3==0:
                answer.append("Fizz")
            elif temp%5==0:
                answer.append("Buzz")
            else:
                answer.append(str(temp))
        return answer



