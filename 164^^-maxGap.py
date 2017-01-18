'''
164. Maximum Gap
Total Accepted: 27628 Total Submissions: 106634 Difficulty: Hard

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        # clean data and check for basic cases
        num=list(set(num))
        if len(num) < 2:
            return 0
        if len(num)==2:
            return abs(num[1]-num[0])

        #set up bins for the numbers, n bins for n numbers
        lowest=min(num)
        highest=max(num)
        interval=float(highest-lowest)/(len(num)-1)
        bins=[[]for i in range((len(num)))]

        #put numbers in bins
        for i in num:
            bins[int((i-lowest)/(interval))].append(i)

        # set maxGap to -1 so we can check whether it gets updated at all in the first while loop
        maxGap=-1
        i=0
        while i <len(bins)-1:
            # detect empty bin, find the difference on two sides.
            # you can improve speed by finding the largest bin-gap, and only calculate for those gaps.  I guess that
            # wouldn't be a huge improve, and would depend on cases.
            if bins[i] and not bins[i+1]:
                low=max(bins[i])
                i+=1
                while i<len(bins) and not bins[i]:
                    i+=1
                if i< len(bins):
                    high=min(bins[i])
                    if maxGap<high-low:
                        maxGap=high-low
            else:
                i+=1

        # if the first  loop did not update maxGap, then each bin has one element.  That means all elememnts are 
        # bin-sorted, things become simple
        if maxGap==-1:
            maxGap=max([bins[i][0]-bins[i-1][0] for i in xrange(1, len(bins))])

        return maxGap


    def maximumGapOld(self, num):
        if len(num) < 2:
            return 0
        if len(num)==2:
            return abs(num[1]-num[0])

        lowest=min(num)
        highest=max(num)
        
        interval=(highest-lowest)/(len(num)-1)
        mode=(highest-lowest) % (len(num)-1)

        bins=[[]for i in range((len(num)-1))]

        # print lowest, highest

        for i in num[:len(num)]:
            if i==highest:
         	   continue
            if i-lowest<=mode*(interval+1):
                # print i, (i-lowest)/(interval+1)
                bins[(i-lowest)/(interval+1)].append(i)
            else:
                # print i,mode+(i-lowest-(interval+1)*mode)/interval
                bins[mode+(i-lowest-(interval+1)*mode)/interval].append(i)


        # return bins

        maxGap=0
        low=lowest
        for bin in bins:
            if bin:
                gap=min(bin)-low
                if gap > maxGap:
                    maxGap=gap
                if len(bin)==2 and max(bin)-min(bin) > maxGap:
                    maxGap=max(bin)-min(bin)
                low=max(bin)

        if highest-low > maxGap:
        	maxGap=highest-low

        return maxGap





if __name__=="__main__":
    solution=Solution()
    # print solution.maximumGap([2,4,5,7,10,11])
    print solution.maximumGap([100,3,2,1])
    print solution.maximumGap([3,6,9,1])

            

        