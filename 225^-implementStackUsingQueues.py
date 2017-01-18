'''
225. Implement Stack using Queues
Total Accepted: 29964 Total Submissions: 98537 Difficulty: Easy

Implement the following operations of a stack using queues.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    empty() -- Return whether the stack is empty.

Notes:

    You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
    Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
    You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

Update (2015-06-11):
The class name of the Java function had been updated to MyStack instead of Stack. 
'''
"""

leaving pop() O(n) time or push() O(n) time is trivial.

here is an O(1) for all solution:



这个算法在本质上，其实就是用很多的queue，做一个list。那么这样其实就是trivial的。巧妙在于把list的queue再组织成一个queue，掩盖了其list的本质。

"""
import Queue
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q=Queue.Queue()
        self.size=0

        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        newQ=Queue.Queue()
        newQ.put(x)
        newQ.put(self.q)
        self.q=newQ
        self.size+=1
        

    def pop(self):
        """
        :rtype: nothing
        """
        elem=self.q.get()
        self.q=self.q.get()
        self.size-=1
        return elem
        

    def top(self):
        """
        :rtype: int
        """
        elem=self.q.get()
        self.q=self.q.get()
        self.push(elem)
        self.size-=1

        return elem

        

    def empty(self):
        """
        :rtype: bool
        """
        return self.size==0


if __name__ == '__main__':
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print s.empty()
    print s.top()
    print s.pop()
    print s.pop()
    print s.pop()
    print s.empty()
    s.push(4)
    print s.top()
        