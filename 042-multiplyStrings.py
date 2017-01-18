
class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string

    # this beats ~65% on leetcoce. faster submissions seem to be frauding with one line solution:
    # return str((int(num1))*(int(num2)))
    # since python supports arbitary length int.


    def multiply(self, num1, num2):
        l1,l2=len(num1),len(num2)
        num1List,num2List=[int(c) for c in num1],[int(c) for c in num2]
        results=[0]*(l1+l2)

        for i2 in xrange(l2):
            for i1 in xrange(l1):
                results[i1+i2+1]+=num1List[i1]*num2List[i2]

        for i in xrange(len(results)-1, 0, -1):
            results[i-1]+=results[i]/10
            results[i]%=10

        i=0
        while i< len(results) and results[i]==0:
            i+=1
        return ''.join(`v` for v in results[i:]) if i < len(results) else '0'







            







    import bisect

    def multiplyOld(self, num1, num2):
        l1,l2=len(num1),len(num2)
        num1List,num2List=[int(c) for c in num1],[int(c) for c in num2]
        result=[0 for i in xrange(l1+l2)]


        for i1 in xrange(len(num1)):
            for i2 in xrange(len(num2)):
                product=num1List[i1]*num2List[i2]
                c2,c1=product/10,product%10
                # print c2,c1
                first=result[-1-(len(num1)-1-i1)-(len(num2)-1-i2)]+c1
                second=result[-1-(len(num1)-1-i1)-(len(num2)-1-i2)-1]+c2
                # print first, second,-1-(len(num1)-1-i1)-(len(num2)-1-i2)
                # print result[-1-(len(num1)-1-i1)-(len(num2)-1-i2)-1]
                result[-1-(len(num1)-1-i1)-(len(num2)-1-i2)]=first%10
                result[-1-(len(num1)-1-i1)-(len(num2)-1-i2)-1]=(second+first/10)%10

                next=-1-(len(num1)-1-i1)-(len(num2)-1-i2)-2
                carry=(second+first/10)/10
                while(carry>0):
                    result[next]+=1
                    carry=result[next]/10
                    result[next]=result[next]%10
                    next-=1



        if [j for j,n in enumerate(result) if n>0]:
            start=[j for j,n in enumerate(result) if n>0][0]
        else:
            return '0'
        # print result
        return ''.join(map(str,result[start:]))

if __name__=="__main__":
    solution=Solution()
    print solution.multiply('9','99')

    print solution.multiply('91','11')
    print solution.multiply('91','0')
    print solution.multiply('100','400')



