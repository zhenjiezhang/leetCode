'''
251. Flatten 2D Vector
Total Accepted: 6250 Total Submissions: 19283 Difficulty: Medium

Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

Hint:

    How many variables do you need to keep track?
    Two variables is all you need. Try with x and y.
    Beware of empty rows. It could be the first few rows.
    To write correct code, think about the invariant to maintain. What is it?
    The invariant is x and y must always point to a valid point in the 2d vector. Should you maintain your invariant ahead of time or right when you need it?
    Not sure? Think about how you would implement hasNext(). Which is more complex?
    Common logic in two different places should be refactored into a common method.

Follow up:
As an added challenge, try to code it using only iterators in C++ or iterators in Java. 
'''


class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.data=vec2d
        i=0
        while i< len(vec2d) and not vec2d[i]:
            i+=1
        if i!= len(vec2d):
            self.currentVec=i
            self.currentIdx=0
        else:
            self.currentVec=-1
            self.currentIdx=-1



    def next(self):
        tmp=self.data[self.currentVec][self.currentIdx]
        if self.currentIdx<len(self.data[self.currentVec])-1:
            self.currentIdx+=1
            return tmp
        self.currentVec+=1
        while self.currentVec<len(self.data) and not self.data[self.currentVec]:
            self.currentVec+=1
        if self.currentVec==len(self.data):
            self.currentVec=-1
            self.currentIdx=-1
        else:
            self.currentIdx=0
        return tmp





    def nextOld(self):
        """
        :rtype: int
        """
        if self.currentVec!=-1:
            result=self.data[self.currentVec][self.currentIdx]
            if self.currentIdx<len(self.data[self.currentVec])-1:
                self.currentIdx+=1
            elif self.currentVec < len(self.data)-1:
                self.currentVec+=1
                while self.currentVec< len(self.data) and not self.data[self.currentVec]:
                    self.currentVec+=1
                
                if self.currentVec!=len(self.data):
                    self.currentIdx=0
                else:
                    self.currentVec=-1
                    self.currentIdx=-1

            else:
                self.currentVec=-1
                self.currentIdx=-1
            return result
        


    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.currentVec!=-1 else False

if __name__ == '__main__':
    v2d=Vector2D([
        [1],
        [2,3]
        ])

    
    while v2d.hasNext(): 
        print v2d.next()
            

        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())