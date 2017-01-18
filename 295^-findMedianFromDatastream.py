'''
295. Find Median from Data Stream
Total Accepted: 10461 Total Submissions: 49231 Difficulty: Hard

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
Examples:

[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

    void addNum(int num) - Add a integer number from the data stream to the data structure.
    double findMedian() - Return the median of all elements so far.

For example:

add(1)
add(2)
findMedian() -> 1.5
add(3) 
findMedian() -> 2

'''
from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.large=[]
        self.small=[]


    def addNum(self, num):
        if not self.large or num>=self.large[0]:
            heappush(self.large, num)
            if len(self.large)>len(self.small)+1:
                heappush(self.small, -heappop(self.large))
        else:
            heappush(self.small, -num)
            if len(self.large)<len(self.small):
                heappush(self.large, -heappop(self.small))
            

    def findMedian(self):

        if len(self.large)==len(self.small):
            return (self.large[0]-self.small[0])/2.0
        return  self.large[0] if len(self.large)>len(self.small) else -self.small[0]

if __name__ == '__main__':
    mf = MedianFinder()
    mf.addNum(-1)
    mf.addNum(-2)
    mf.addNum(-3)
    mf.addNum(-4)

    print mf.findMedian()
        

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()