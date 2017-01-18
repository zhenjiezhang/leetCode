'''
34. Search for a Range
Total Accepted: 69125 Total Submissions: 244784 Difficulty: Medium

Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4]. 
'''
'''




Code up this one:

vector<int> searchRange(vector<int>& nums, int target) {
    int idx1 = lower_bound(nums, target);
    int idx2 = lower_bound(nums, target+1)-1;
    if (idx1 < nums.size() && nums[idx1] == target)
        return {idx1, idx2};
    else
        return {-1, -1};
}

int lower_bound(vector<int>& nums, int target) {
    int l = 0, r = nums.size()-1;
    while (l <= r) {
        int mid = (r-l)/2+l;
        if (nums[mid] < target)
            l = mid+1;
        else
            r = mid-1;
    }
    return l;
}
'''
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        v1=self.findInseartion(A, target)
        v2=self.findInseartion(A, target+1)-1
        # print v1, v2
        return [v1, v2] if v1<len(A) and A[v1]==target else [-1,-1]

    def findInseartion(self,A,target):
        left, right=0, len(A)-1
        while left<=right:
            mid=(right+left)/2
            # print left, right, mid

            if A[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left



    def searchRangeOld(self, A, target):
    	firstHit=len(A)>>1

    	left,right=0,len(A)

    	while left!=right and A[firstHit]!=target:
    		if A[firstHit]<target:
    			left=firstHit+1
    			firstHit=(left+right)>>1
    		else:
    			right=firstHit
    			firstHit=(left+right)>>1

    	if left==right:
    		return [-1,-1]

    	left, right=0,firstHit

    	leftBound=(left+right)>>1
    	while left!=right and (A[leftBound]==target and (leftBound==0 or A[leftBound-1]<target))==False:
    		if A[leftBound]<target:
    			left=leftBound+1
    			leftBound=(left+right)>>1
    		else:
    			right=leftBound
    			leftBound=(left+right)>>1

    	left,right=firstHit,len(A)
    	rightBound=(left+right)>>1
    	while left!=right and (A[rightBound]==target and (rightBound==len(A)-1 or A[rightBound+1]>target))==False:
    		if A[rightBound]>target:
    			right=rightBound
    			rightBound=(left+right)>>1
    		else:
    			left=rightBound+1
    			rightBound=(left+right)>>1

    	return [leftBound,rightBound]

if __name__=="__main__":
	solution=Solution()
	print solution.searchRange([1,1,1,2,3,3,4,5,5],5)
	print solution.searchRange([],5)

