'''
153. Find Minimum in Rotated Sorted Array
Total Accepted: 76974 Total Submissions: 218874 Difficulty: Medium

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if len(num)<=2:
            return min(num)

        if num[0]< num[-1]:
            return num[0]

        middle=len(num)/2

        if num[middle] < num[-1]:
            return self.findMin(num[:middle+1])
        else:
            return self.findMin(num[middle+1:])


if __name__=="__main__":
    print Solution().findMin([8,9,10,10,10,10,10,10,0,1,2,3,4,5,6,6,6,6,6,6,7])
    print Solution().findMin([1,1,3])
    print Solution().findMin([1,1,1,1])
    print Solution().findMin([7,7,7,7,8,9,10,10,10,10,10,10,0,1,2,3,4,5,6,6,6,6,6,6,7,7,7,7,7])
        




