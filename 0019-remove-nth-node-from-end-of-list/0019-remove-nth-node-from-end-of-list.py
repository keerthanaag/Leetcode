# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        cur = head
        size = 0
        while cur != None:
            size += 1
            cur = cur.next
        indx = size - n +1
        pos = 0
        cur = head
        print(size,indx)
        if indx == 1:
            print("head")
            head = head.next
        elif indx == size:
            print("delete at end")
            while cur.next and cur.next.next:
                cur = cur.next
            cur.next = None
        else:
            print("delete at middle")
            pos = 1
            while cur.next and pos+1 != indx:
                cur = cur.next
                pos += 1
            cur.next = cur.next.next
        return head
        
        