# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        nod=attach=ListNode(0)
        p1=l1
        p2=l2

        while p1 and p2:
            if p1.val>p2.val:
                attach.next=p2
                p2=p2.next
            else:
                attach.next=p1
                p1=p1.next

            attach=attach.next


        
        
        if not p1:
            attach.next=p2
            
        if not p2:
            attach.next=p1
        

        return nod.next

if __name__ == '__main__':
    l1=ListNode(1)
    l2=ListNode(2)
    solution=Solution()
    print solution.mergeTwoLists(l1,l2).val



