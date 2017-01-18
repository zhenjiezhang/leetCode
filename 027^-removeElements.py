'''
27. Remove Element
Total Accepted: 94075 Total Submissions: 288589 Difficulty: Easy

Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length. 




 public class Solution {
     public int removeElement(int[] nums, int val) {
       if(nums==null || nums.length==0){
           return 0;
       } 
       int start = 0;
       int end = nums.length-1;
       while(start<=end){
           if(nums[start]==val){
               nums[start] = nums[end];
               end--;
           }
           else{
               start++;
           }
       }
       return end+1;
     }
 }
'''
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if not A:
            return 0

        head, tail=0, len(A)-1
        while head <= tail:
            while head <= tail and A[head]!=elem:
                head+=1

            while head<=tail and A[tail]==elem:
                tail-=1

            if head<tail:
                A[head]=A[tail]
                head+=1
                tail-=1
        return head






    def removeElementOld(self, A, elem):
        i=0
        while i<len(A) and A[i]!=elem:
            i+=1
        if i< len(A):
            ins=i
        else:
            return len(A)

        while i < len(A):
            if A[i]!=elem:
                A[ins]=A[i]
                ins+=1
            i+=1

        return ins

if __name__ == '__main__':
    solution=Solution()
    print solution.removeElement([2,3,4,2,3,4,3],3)
    print solution.removeElement([1],2)
    print solution.removeElement([4,5],4)
