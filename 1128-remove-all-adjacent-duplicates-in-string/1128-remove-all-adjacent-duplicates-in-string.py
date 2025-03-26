from collections import deque
class Solution(object):
    def removeDuplicates(self, s):
        stack = deque()
        for i in range(len(s)):
            print(i,s[i])
            if i == 0:
                stack.append(s[i])
            else:
                if len(stack) != 0:
                    prev = stack.pop()
                    if prev != s[i]:
                        stack.append(prev)
                        stack.append(s[i])
                else:
                    stack.append(s[i])
        print(stack)
        print("".join(list(stack)))
        return "".join(list(stack))