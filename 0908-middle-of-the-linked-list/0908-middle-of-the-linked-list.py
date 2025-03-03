# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.node=head
        self.size=1
        # to get the size of the linked listhead
        while self.node.next != None:
            self.size+=1
            self.node=self.node.next
        print("size: ",self.size)
        # to store the new elements from the node
        mid = (self.size//2)+1
        print(mid)
        self.node=head
        self.pos = 1
        while self.node.next != None and self.pos != mid:
            self.pos +=1
            self.node=self.node.next
        
        return self.node


            

        