# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        cur = head
        while cur != None :
            print(cur.val)
            if head.val == val:
                if head.next != None:
                    head = head.next
                    cur = head
                    continue
                else:
                    head = None
            if cur.next != None and cur.next.val == val :
                if cur.next.next == None:
                    cur.next = None
                else:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return head