'''274. H-Index
Total Accepted: 24588 Total Submissions: 86414 Difficulty: Medium

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.

Hint:

    An easy approach is to sort the array first.
    What are the possible values of h-index?
    A faster approach is to use extra space.

'''


class Solution(object):

    def hIndex(self, citations):
        citations=sorted(citations)[::-1]
        for i in xrange(len(citations)):
            if citations[i]<i+1:
                return i
        return len(citations)


    # this is actually same to the naive sorting solution, but using a partial bucket sorting mechanism.
    def hIndexOld(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        relevantList=[0 for i in xrange(len(citations)+1)]
        qualifiedPubs=0
        for c in citations:
        	if c<=len(citations):
        		relevantList[c]+=1
        	else:
        		qualifiedPubs+=1

        i=len(citations)+1
        while qualifiedPubs < i:
        	i-=1
        	qualifiedPubs+=relevantList[i]

        return i

if __name__=='__main__':
	print Solution().hIndex([3,0,6,1,5])
	print Solution().hIndex([])


