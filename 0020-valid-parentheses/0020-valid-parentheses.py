class Solution:
    def isValid(self, s: str) -> bool:
        opcl = dict(('()', '[]', '{}'))
        stack = []
        lst=['(','[','{']
        for x in s:
            if x in lst:
                stack.append(x)
            elif len(stack)==0 or x != opcl[stack.pop()]:
                return False
        return len(stack) == 0
        




        