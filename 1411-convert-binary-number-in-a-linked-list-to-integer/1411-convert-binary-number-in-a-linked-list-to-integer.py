# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node=head
        ans=''
        while node.next != None:
            ans+=str(node.val)
            node=node.next
        ans+=str(node.val)
        print(ans)
        num=0
        for i in range(len(ans)):
            if ans[i] == '1':
                power=len(ans)-1-i
                num+=(2**power)
            #print(ans,len(ans)-1-i)
        print(num)
        return num        