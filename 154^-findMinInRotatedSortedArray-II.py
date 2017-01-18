'''
154. Find Minimum in Rotated Sorted Array II
Total Accepted: 44330 Total Submissions: 132110 Difficulty: Hard

    Follow up for "Find Minimum in Rotated Sorted Array":
    What if duplicates are allowed?

    Would this affect the run-time complexity? How and why?

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
'''

class Solution:
    # @param num, a list of integer
    # @return an integer

    #slightly slower than the old version, but much easier to write
    def findMin(self, num):
        if len(num)<=2:
            return min(num)

        middle=len(num)/2
        if num[middle]==num[0] and num[middle] ==num[-1]:
            leftMin=self.findMin(num[:middle+1])
            return leftMin if leftMin < num[0] else self.findMin(num[middle+1:])

        if num[middle] <= num[-1] and num[middle] >= num[0]:
            return num[0]

        if num[middle] < num[0]:
            return self.findMin(num[:middle+1])
        else:
            return self.findMin(num[middle+1:])


            



    def findMinOld(self, num):
        if len(num)<=2:
            return min(num)


        middle=num[len(num)/2]
        # print middle
        if middle==num[0] and middle ==num[len(num)-1]:
            probe=len(num)/2
            while(probe >= 0 and num[probe]==middle):
                probe-=1
            if probe>=0:
                return self.findMin(num[:probe+1])
            else:
                probe=len(num)/2
                while(probe < len(num)-1 and num[probe]==middle):
                    probe+=1
                
                return self.findMin(num[probe:])


        if middle <= num[len(num)-1] and middle >= num[0]:
            return num[0]

        if middle <= num[len(num)-1] and middle <= num[0]:
            return self.findMin(num[:len(num)/2+1])
        if middle >= num[len(num)-1] and middle >= num[0]:
            return self.findMin(num[len(num)/2+1:])