'''
281. Zigzag Iterator
Total Accepted: 6107 Total Submissions: 14893 Difficulty: Medium

Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question - Update (2015-09-18):
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:

[1,2,3]
[4,5,6,7]
[8,9]



'''
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        result=[]
        for a1,a2 in zip(v1, v2):
            result.extend([a1, a2])
        if len(v1)>len(v2):
            result.extend(v1[len(v2):])
        elif len(v2)>len(v1):
            result.extend(v2[len(v1):])

        self.p=0
        self.result=result

    def next(self):
        """
        :rtype: int
        """
        self.p+=1
        return self.result[self.p-1]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.p<len(self.result)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())