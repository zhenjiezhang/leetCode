'''
57. Insert Interval
Total Accepted: 49726 Total Submissions: 217687 Difficulty: Hard

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10]. 
'''


#`neater:
# vector<Interval> insert(vector<Interval> &intervals, Interval newInterval) {
#     vector<Interval> ret;
#     int i,n=intervals.size();
#     Interval mergeInterval = newInterval;
#     for(i=0;i<n;i++){
#         if(newInterval.start>intervals[i].end)
#             ret.push_back(intervals[i]);
#         else if(newInterval.end<intervals[i].start)
#             break;
#         else
#             mergeInterval = Interval(min(mergeInterval.start,intervals[i].start)
#             ,max(mergeInterval.end,intervals[i].end));
#     }
#     ret.push_back(mergeInterval);
#     for(;i<n;i++)
#         ret.push_back(intervals[i]);
#     return ret;
# }






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


from bisect import bisect
class Solution:
    def insert(self, intervals, newInterval):
        intervals=[[i.start, i.end] for i in intervals]
        newInterval=[newInterval.start, newInterval.end]
        pos=bisect(intervals, newInterval)

        if pos<len(intervals) and intervals[pos][0]<=newInterval[1]:
            intervals[pos]=[newInterval[0], max(intervals[pos][1], newInterval[1])]
        elif pos>0 and newInterval[0]<=intervals[pos-1][1]:
            intervals[pos-1]=[intervals[pos-1][0], max(intervals[pos-1][1], newInterval[1])]
        else:
            return intervals[:pos]+[newInterval]+intervals[pos:]

        results=[]
        i=0
        while i<len(intervals):
            results.append(intervals[i])
            while i+1 < len(intervals) and intervals[i+1][0]<=results[-1][1]:
                results[-1][1]=max(intervals[i+1][1], results[-1][1])
                i+=1
            i+=1
        return results


            






    def insertOld(self, intervals, newInterval):
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


if __name__=="__main__":
    solution=Solution()
    print solution.insert([Interval(3,6)], Interval(4,5))
    print solution.insert([Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)],Interval(4,9))
    # print solution.insert([Interval()], Interval(5,7)
