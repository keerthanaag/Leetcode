# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        self.h = None
        while cur != None:
            data = cur.val
            if self.h == None:
                self.h = ListNode(data)
            else:
                new = ListNode(data)
                new.next = self.h
                self.h = new
            print(cur.val)
            cur = cur.next
        return self.h
        
        
        