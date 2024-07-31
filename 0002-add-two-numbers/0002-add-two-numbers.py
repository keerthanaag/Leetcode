# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        div = 0
        la = l1
        lb = l2
        temp_node = lc = ListNode(0)
        while la or lb:
            a = b = 0  
            if not la:
                la = ListNode(0)
            a = la.val
            if not lb:
                lb = ListNode(0)
            b = lb.val
            temp1 = a + b + div
            rem = temp1 % 10
            div = temp1 // 10
            lc.val = rem  #4
            if div == 1:
               lc.next = ListNode(1)
            else:
                if la.next or lb.next:
                   lc.next = ListNode(0)
            la = la.next
            lb = lb.next
            lc = lc.next
        return temp_node