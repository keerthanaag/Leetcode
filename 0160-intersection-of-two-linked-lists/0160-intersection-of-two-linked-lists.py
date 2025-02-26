# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA, curB = headA, headB
        
        while curA != curB:

            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        
        return curA
        
        curA = headA
        curB = headB
        while curA != None:
            curB = headB
            while curB != None :
                print(curA.val,curB.val)
                if curA == curB :
                    print(curA.val)
                    return curA
                curB = curB.next
            curA = curA.next
            
        return None
        