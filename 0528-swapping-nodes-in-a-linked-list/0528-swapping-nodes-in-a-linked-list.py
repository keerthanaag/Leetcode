# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # calculating the size of the linked list and storing its value in list
        lst = []
        size = 0
        cur = head
        while cur != None:
            size += 1
            lst.append(cur.val)
            cur = cur.next
        print(size,lst)
        # updating the values based on k
        cur = head
        pos = 1
        while cur != None:
            print(cur.val)
            if pos == k :
                cur.val = lst[(size - k + 1)-1]
            elif pos == (size - k + 1):
                cur.val = lst[k-1]
            pos += 1
            cur = cur.next
        return head
        