'''
275. H-Index II
Total Accepted: 17517 Total Submissions: 54348 Difficulty: Medium

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Hint:

    Expected runtime complexity is in O(log n) and the input is sorted.


    '''
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
        	return 0

        n=len(citations)

        l,r=0,n
        m=(l+r)/2

        while citations[m]!=n-m and l<r-1:
        	if citations[m]>=n-m and (m==0 or citations[m-1]<1+n-m):
        		return n-m


        	if citations[m]>n-m:
        		r=m
        	else:
        		l=m
        	m=(l+r)/2

        if l==r-1:
        	return n-l if citations[l]>=n-l else n-l-1



        return n-m

if __name__=='__main__':
	print Solution().hIndex([1])

