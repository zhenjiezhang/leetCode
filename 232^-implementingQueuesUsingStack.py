'''
232. Implement Queue using Stacks
Total Accepted: 32197 Total Submissions: 94957 Difficulty: Easy

Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.

Notes:

    You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
    You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).


    究其本质，就是负负得正。倒过来的东西，再倒一次，就是正的。别想复杂了。而用queue造stack因为不能正正得负，所以要用不同的策略。

    '''
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ip=[]
        self.op=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.ip.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.move()
        return self.op.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.op[-1]

        

    def empty(self):
        """
        :rtype: bool
        """
        return not bool (self.ip or self.op)

    def move(self):
        if not self.op:
            while self.ip:
                self.op.append(self.ip.pop())
        