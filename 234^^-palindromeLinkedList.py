'''
234. Palindrome Linked List
Total Accepted: 36217 Total Submissions: 136297 Difficulty: Easy

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?


这个太牛了！

class Solution {
public:
    ListNode* temp;
    bool isPalindrome(ListNode* head) {
        temp = head;
        return check(head);
    }

    bool check(ListNode* p) {
        if (NULL == p) return true;
        bool isPal = check(p->next) & (temp->val == p->val);
        temp = temp->next;
        return isPal;
    }
};

本质上，就是利用回归层层上推，同时利用全局变量层层下推。

another way:
two pointers, p1 and p2, p2 goes doubling the speed of p1, and p1 reverses the order as it goes.  when p2 reaches the end, put it back to the head, then p1 and p2 should go over the same values.


'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """


        n=0
        p=head

        while p:
            n+=1
            p=p.next

        if n<2:
            return True

        p1=head
        p2=head.next

        count=1

        while count<n//2:
            tmp=p2.next
            p2.next=p1
            p1=p2
            p2=tmp

            count+=1

        head.next=None
        if n%2==1:
            p2=p2.next

        while p1 and p2 and p1.val==p2.val:

            p1,p2=p1.next, p2.next


        return not p1

if __name__ == '__main__':
    head=ListNode(1)
    head.next=ListNode(2)
    head.next.next=ListNode(2)
    head.next.next.next=ListNode(1)

    print Solution().isPalindrome(head)

        