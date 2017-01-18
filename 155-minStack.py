'''
155. Min Stack
Total Accepted: 58704 Total Submissions: 275562 Difficulty: Easy

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

    '''

class MinStack:
    # @param x, an integer
    def __init__(self):
    	self.stack=[]
    	self.min=[]

    # @return an integer

    def push(self, x):
    	self.stack.append(x)
    	if not self.min:
    		self.min.append(x)
    	else:
    		self.min.append(min(x,self.min[-1]))
        

    # @return nothing
    def pop(self):
    	self.stack.pop()
    	self.min.pop()
        

    # @return an integer
    def top(self):
    	return self.stack[-1] if self.stack else 0
        

    # @return an integer
    def getMin(self):
    	return self.min[-1] if self.min else 0
        