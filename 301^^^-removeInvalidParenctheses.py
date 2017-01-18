'''
301. Remove Invalid Parentheses
Total Accepted: 8120 Total Submissions: 26326 Difficulty: Hard

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:

"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]

'''

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        head=[]
        tail=[]
        i=0
        while i < len(s) and s[i]!='(':
            if s[i]!=')':
                head.append(s[i])
            i+=1
        start=i
        head=''.join(head)

        i=len(s)-1
        while i>=0 and s[i]!=')':
            if s[i]!='(':
                tail.append(s[i])
            i-=1
        end=i
        tail=''.join(tail)[::-1]




        if start>end:
            return [head+tail[start-end-1:]]

        workS=s[start: end+1]


        openLeft=0
        boundForLeft=0
        for i in xrange(len(workS)):
            if workS[i]=='(':
                openLeft+=1
            elif workS[i]==')' and openLeft>0:
                openLeft-=1

            if openLeft==0:
                boundForLeft=i+1

        openRight=0
        boundForRight=len(workS)-1
        for i in xrange(len(workS)-1,-1,-1):
            if workS[i]==')':
                openRight+=1
            elif workS[i]=='(' and openRight>0:
                openRight-=1

            if openRight==0:
                boundForRight=i-1

        if openLeft:
            partialResults=self.removeLeftAndRight(workS, boundForLeft, boundForRight, openLeft, openRight)
        else:
            reverseWorkS= ''.join([a if a!='(' and a!=')' else ('(' if a==')' else ')') for a in workS[::-1]])

            partialResults=self.removeLeftAndRight(reverseWorkS, len(workS)-1-boundForRight, len(workS)-1-boundForLeft, openRight, openLeft)
            partialResults=[''.join([a if a!='(' and a!=')' else ('(' if a==')' else ')') for a in p[::-1]]) for p in partialResults]

        results=[head+st+tail for st in partialResults if self.valid(st)]
        return results

    def valid(self,s):
        left=0
        for c in s:
            if c=='(':
                left+=1
            elif c==')':
                left-=1
            if left<0:
                return False
        return left==0

    def removeLeftAndRight(self, s, boundForLeft, boundForRight, extraLeft, extraRight):
        results=[]
        # print boundForLeft, boundForRight,  extraLeft, extraRight
        if extraLeft==0:
            return [s]

        i=0
        while i < len(s) and not (s[i]=='(' and i>=boundForLeft and extraLeft>0) and not \
            (s[i]==')' and i<=boundForRight and extraRight>0):
            i+=1

        if i < len(s) and s[i]=='(':
            l=i+1
            while s[l]=='(':
                l+=1
            stretch=l-i 
            for leftRemoved in xrange(min(stretch,extraLeft)+1):

                thisPartialResults=(self.removeLeftAndRight(s[l:], boundForLeft-l, \
                    boundForRight-l, extraLeft-leftRemoved, extraRight))
                results.extend([s[:l-leftRemoved]+st for st in thisPartialResults])

        elif i < len(s) and s[i]==')':
            r=i+1

            while r <=boundForRight and s[r]==')':
                r+=1
            stretch=r-i
            for rightRemoved in xrange(min(stretch, extraRight)+1):

                thisPartialResults=self.removeLeftAndRight(s[r:], boundForLeft-r, \
                    boundForRight-r, extraLeft, extraRight-rightRemoved)
                results.extend([s[:r-rightRemoved]+st for st in thisPartialResults])

        return results


if __name__ == '__main__':
    solution=Solution()
    print solution.removeInvalidParentheses("(a)())()")
    print solution.removeInvalidParentheses(")(")
    print solution.removeInvalidParentheses("())")
    print solution.removeInvalidParentheses("(()")

    # print solution.removeInvalidParentheses("n")



    print solution.removeInvalidParentheses("(((()(()")


