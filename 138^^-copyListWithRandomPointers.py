'''
138. Copy List with Random Pointer
Total Accepted: 56383 Total Submissions: 218101 Difficulty: Hard

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list. 



'''
'''


This is none-dict method:


I thought the same way, did not implement:



class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode * head) {
        RandomListNode * head_cp = nullptr, * cur = head, * cur_cp = nullptr;
        if (head == nullptr)
            return nullptr;
        while (cur != nullptr)
        {
            cur_cp = new RandomListNode (cur->label);
            cur_cp->next = cur->next;
            cur->next = cur_cp;
            cur = cur_cp->next;
        }
        cur = head;
        while (cur != nullptr)
        {
            cur_cp = cur->next;
            if (cur->random)
                cur_cp->random = cur->random->next;
            cur = cur_cp ->next;
        }
        cur = head;
        head_cp = head->next;
        while (cur != nullptr)
        {
            cur_cp = cur->next;
            cur->next = cur_cp->next;
            cur = cur->next;
            if (cur)
                cur_cp->next = cur->next;
        }
        return head_cp;
    }
};



'''
# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None

        nodeS=head
        res=nodeD=RandomListNode(head.label)
        nodeMap={head: nodeD}

        while nodeS:
            if nodeS.next:
                if nodeS.next in nodeMap:
                    nodeD.next=nodeMap[nodeS.next]
                else:
                    nodeD.next=RandomListNode(nodeS.next.label)
                    nodeMap[nodeS.next]=nodeD.next
            if nodeS.random:
                if nodeS.random in nodeMap:
                    nodeD.random=nodeMap[nodeS.random]
                else:
                    nodeD.random=RandomListNode(nodeS.random.label)
                    nodeMap[nodeS.random]=nodeD.random
            nodeS=nodeS.next
            nodeD=nodeD.next
        return res



    def copyRandomListOld(self, head):
        if not head:
        	return None

        sourceNodes=dict()
        nodeOrder=0

        destNodes=[]

        newHead=RandomListNode(head.label)

        sourceIter=head
        destIter=newHead

        sourceNodes[sourceIter]=nodeOrder
        destNodes.append(destIter)

        while sourceIter.next:
        	sourceIter=sourceIter.next
        	nodeOrder+=1
        	sourceNodes[sourceIter]=nodeOrder

        	destIter.next=RandomListNode(sourceIter.label)
        	destIter=destIter.next
        	destNodes.append(destIter)

        sourceIter=head
        destIter=newHead

        while sourceIter:
        	if sourceIter.random:
        		destIter.random=destNodes[sourceNodes[sourceIter.random]]
        	if sourceIter.next:
        		sourceIter=sourceIter.next
        		destIter=destIter.next
        	else:
        		break

        return newHead

if __name__=="__main__":
	solution=Solution()
	r1=RandomListNode(1)
	r2=RandomListNode(2)
	r3=RandomListNode(3)
	r4=RandomListNode(4)
	r5=RandomListNode(5)

	r1.next=r2
	r2.next=r3
	r3.next=r4
	r4.next=r5

	r1.random=r3
	r2.random=r4
	# r3.random=r5
	# r4.random=r1
	r5.random=r2

	r=solution.copyRandomList(r1)
	# r=r1
	while r:
		print r.label,r.random.label if r.random else ""
		if r.next:
			r=r.next
		else:
			break





