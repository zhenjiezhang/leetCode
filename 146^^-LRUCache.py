'''
146. LRU Cache
Total Accepted: 60937 Total Submissions: 389465 Difficulty: Hard

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item. 
'''

# version without using double linked chain
from collections import deque
class LRUCache(object):

    def __init__(self, capacity):

        self.capacity=capacity
        self.data=dict()
        self.ocurrenceInHistory=dict()
        self.history=deque()


    def get(self, key):

        if key not in self.data:
            return -1
        self.ocurrenceInHistory[key]+=1
        self.history.append(key)
        return self.data[key]
        

    def set(self, key, value):

        if key not in self.data and len(self.data) == self.capacity:
            keyToDel=self.history.popleft()
            while self.ocurrenceInHistory[keyToDel]>1:
                self.ocurrenceInHistory[keyToDel]-=1
                keyToDel=self.history.popleft()

            self.ocurrenceInHistory.pop(keyToDel,0)
            self.data.pop(keyToDel,0)
        
        self.data[key]=value
        self.ocurrenceInHistory[key]=1 if key not in self.ocurrenceInHistory else self.ocurrenceInHistory[key]+1
        self.history.append(key)





# double linked list and map.  Can be imporved by using headCap and tailCap to simplify insertion and 
# deletion.  Also, move some repeated codes to seperate functions.
class node:
    def __init__(self,key,val):
        self.val=val
        self.key=key
        self.pre=None
        self.next=None


class LRUCacheOld:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity=capacity
        self.keyDict={}
        self.head=None
        self.tail=None


    # @return an integer
    def get(self, key):
        if key in self.keyDict:
            curNode=self.keyDict[key]
            if self.head!=curNode:
                curNode.pre.next=curNode.next
                if curNode.next:
                	curNode.next.pre=curNode.pre
                else:
            	    self.tail=curNode.pre
                curNode.next=self.head
                self.head.pre=curNode
                self.head=curNode

            return curNode.val
        else:
            return -1
            
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.keyDict:
            curNode=self.keyDict[key]
            if self.head!=curNode:
                curNode.pre.next=curNode.next
                if curNode.next:
                	curNode.next.pre=curNode.pre
                else:
            	    self.tail=curNode.pre
                curNode.next=self.head
                self.head.pre=curNode
                self.head=curNode
            curNode.val=value

        else:
            # print len(self.keyDict), self.capacity
            if len(self.keyDict)<self.capacity:
                curNode=node(key,value)
                self.keyDict[key]=curNode
                curNode.next=self.head
                if self.head:
                    self.head.pre=curNode
                self.head=curNode
                if not self.tail:
                	self.tail=curNode
            else:
                self.keyDict.pop(self.tail.key,None)
                self.keyDict[key]=self.tail
                self.tail.val=value
                self.tail.key=key
                if self.tail.pre:
                	self.tail.pre.next=None
	                self.tail.next=self.head
	                self.head.pre=self.tail
	                self.head=self.tail
	                self.tail=self.tail.pre


if __name__=="__main__":
    cache=LRUCache(3)
    cache.set(1,1)
    cache.set(2,2)
    cache.set(3,3)
    cache.set(4,4)

    print cache.get(4)



    print cache.get(3)
    print cache.get(2)
    print cache.get(1)
    cache.set(5,5)
    print cache.get(1)
    print cache.get(2)
    print cache.get(3)
    print cache.get(4)
    print cache.get(5)





# head=cache.head
# tail=cache.tail
# print cache.keyDict[3].next.val
# print head.val, tail.val
# print cache.keyDict.keys()
# while head:
#     print head.key, head.val
#     head=head.next



        