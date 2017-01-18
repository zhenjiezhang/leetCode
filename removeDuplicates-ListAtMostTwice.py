class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A)<3:
            return len(A)
        else:
            l,ll=1,0
            probe=2
            while probe<len(A) and (A[l]!=A[ll] or A[probe]!=A[l]):
                ll=l
                l=probe
                probe+=1
            if probe==len(A):
                # print A
                return probe
            terminal=probe
            print terminal
            
        while(probe<len(A)):
            if (A[l]==A[ll] and A[probe]==A[l]):
                while  probe<len(A) and A[probe]==A[ll]:
                    probe+=1
                if probe==len(A):
                    break
            
            A[terminal]=A[probe]
            terminal+=1
            ll+=1
            l+=1
            probe+=1
            # print A[ll:probe+1],probe,A
        for i in xrange(len(A)-1,terminal-1,-1):
            A.pop()
        return len(A)

if __name__=="__main__":
    solution=Solution()
    print solution.removeDuplicates([1,1,1,1,2,2,3])

