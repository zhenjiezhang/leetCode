'''
119. Pascal's Triangle II
Total Accepted: 63362 Total Submissions: 204251 Difficulty: Easy

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space? 
'''


'''
 vector<int> getRow(int rowIndex) {
   vector<int> res(rowIndex + 1, 1);
   for(int k = 1; k <= (rowIndex + 1)/2; k++)
        res[k] = res[rowIndex - k] = (long)res[k - 1]*(long)(rowIndex - k + 1)/k;
   return res;
}
'''



'''
i=0
        result=[1]
        while i <rowIndex:
            next=[1]+[result[j]+result[j+1] for j in xrange(len(result)-1)]+[1]
            result=next
            next=[]
            i+=1
        return result=next
'''


from math import factorial as fact
class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        fn=fact(rowIndex)
        return [fn/fact(i)/fact(rowIndex-i) for i in xrange(rowIndex+1)]


    def getRowOld(self, rowIndex):
        

        i=0
        result=[1]
        while i <rowIndex:
        	next=[1]+[result[j]+result[j+1] for j in xrange(len(result)-1)]+[1]
        	result=next
        	next=[]
        	i+=1
        return result

if __name__ == '__main__':
	print Solution().getRow(3)
