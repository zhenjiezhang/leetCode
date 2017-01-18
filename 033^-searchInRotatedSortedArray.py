'''
33. Search in Rotated Sorted Array
Total Accepted: 84991 Total Submissions: 288035 Difficulty: Hard

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''

class Solution:
    def search(self, inArray, target):
        lastIdx=0
        length=len(inArray)

        left=0
        right=length-1

        if length==1:
            return 0 if inArray[0]==target else -1

        # you will need to check both left and right since later you will being 
        # using left and right to decide the position
        
        while (left<right):
            mid=(left+right)/2
            if target == inArray[mid]:
                return mid
            elif target == inArray[left]:
                return left
            elif target == inArray[right]:
                return right
            elif (right-left)==1:
                return -1

            elif target < inArray[mid]:
                if inArray[mid] < inArray[left]:
                    right=mid-1
                elif target > inArray[left]:
                    right=mid-1
                else:
                    left=mid+1

            else:    #target > inArray[mid]
                if inArray[mid]    < inArray[left]:
                    if target> inArray[right]:
                        right=mid-1
                    else:
                        left=mid+1
                else:
                    left=mid+1



        return -1

if __name__=="__main__":
    solution=Solution()
    print solution.search([1],1)



