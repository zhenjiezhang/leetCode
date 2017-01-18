class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        maxAfter=[[],[]] #index of the maxnums after position i in nums1 and nums2
        inputs=[nums1, nums2]
        # digitStacks to record the position of digits 0-9, for each digit, each nums list.  scan will be 
        # from tail to head, so the each pop will produce the earlist corresponding number in each nums list
        numPositions=[[[] for _ xrange(len(inputs))] for _ in xrange(10)]
        pointers=[0]*len(inputs)


        for n in len(inputs):
            maxFromTail=0
            for i in xrange(len(nums)-1, -1, -1):
                maxAfter[n][i]=maxFromTail
                numPositions[inputs[n][i]][n].append[i]

                if inputs[n][i]>=maxFromTail:
                    maxFromTail=i


        print maxAfter
        print numPositions

        for i in xrange(k):
            for digit in xrange(len(numPositions)-1, -1, -1):

                for positions in numPositions[digit]:


    def nextLargestValid(p1, p2):
        while self.maxAfter[p1]==self.maxAfter[p2]:
            
