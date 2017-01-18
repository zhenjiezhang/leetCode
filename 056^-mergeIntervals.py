
class Interval():
    start=0
    end=0
    def __init__(self, start, end):
        self.start=start
        self.end=end

    def __repr__(self):
        return "["+str(self.start)+","+str(self.end)+"]"

    def __str__(self):
        return "["+str(self.start)+","+str(self.end)+"]"

    # def __cmp__(self, int2):
    #     return cmp([self.start, self.end], [int2.start, int2.end])


# convert to list, and then use the same method is much faster. beats 90%
class Solution:
    def merge(self, intervals):
        intervals=sorted(intervals, cmp=lambda x,y: cmp([x.start, x.end],[y.start, y.end]))

        merged=[]
        i=0
        while i<len(intervals):

            merged.append(intervals[i])
            i+=1
            while i < len(intervals) and intervals[i].start<=merged[-1].end:
                merged[-1].end=max(merged[-1].end, intervals[i].end)
                i+=1

        return merged

'''
Old
'''
    def insert(self, intervals, newInterval):
        left=newInterval.start
        right=newInterval.end
        n=len(intervals)

        lbound=rbound=-1
        lnum=-1
        rnum=n

        if n==0:
            return [newInterval]
        for i in range(len(intervals)):
            if intervals[i].start<left:
                lnum=i

            if (intervals[i].end<=right and intervals[i].end>=left) or (intervals[i].end>right and intervals[i].start<=right):
                lnum=i
                lbound=min(left, intervals[i].start)
                break

        for i in range(len(intervals)-1,-1,-1):
            if intervals[i].end>right:
                rnum=i

            if (intervals[i].start>=left and intervals[i].start<=right) or (intervals[i].start<left and intervals[i].end>=left):
                rnum=i
                rbound=max(right, intervals[i].end)
                break

        if lbound==-1:
            results=intervals[0:lnum+1]+[newInterval]+intervals[rnum:n]
        else:
            results=intervals[0:lnum]+[Interval(lbound,rbound)]+intervals[rnum+1:n]

        return results


    def mergeOld(self, intervals):
        if len(intervals)<2:
            return intervals

        growingIntervals=intervals[0:1]
        for i in range(1,len(intervals)):
            growingIntervals=self.insert(growingIntervals,intervals[i])

        return growingIntervals

if __name__=="__main__":
    solution=Solution()
    print solution.merge([Interval(1,3),Interval(8,10),Interval(2,6),Interval(15,18)])
    print solution.mergeOld([Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)])


