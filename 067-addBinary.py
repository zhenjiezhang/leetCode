'''
67. Add Binary
Total Accepted: 69294 Total Submissions: 265751 Difficulty: Easy

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100". 
'''
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        a=[int(i) for i in a][::-1]
        b=[int(i) for i in b][::-1]

        r=[]
        for i in xrange(min(len(a), len(b))):
            r.append(a[i]+b[i])
        r.extend((a if len(a)>len(b) else b)[i+1:])
        r.append(0)


        for i in xrange(1,len(r)):
            r[i]+=r[i-1]/2
            r[i-1]%=2

        return ''.join([`i` for i in r[::-1]]) if r[-1] else ''.join([`i` for i in r[:-1][::-1]])








    def addBinaryOld(self, a, b):
        if len(a)<len(b):
            tmp=a
            a=b
            b=tmp

        c=0
        r=[]
        res=0
        while c<len(b):
            raw=int(a[len(a)-1-c])+int(b[len(b)-1-c])+res
            if raw==2:
                r.append('0')
                res=1
            elif raw==3:
                r.append('1')
                res=1
            else:
                r.append(str(raw))
                res=0
            c+=1


        if c==len(a):
                r.append('1' if res==1 else '')

        while c<len(a):
            while c<len(a) and res==1:
                raw=int(a[len(a)-1-c])+res
                # print raw
                if raw==2:
                    r.append('0')
                else:
                    r.append('1')
                    res=0
                c+=1
            if c==len(a):
                r.append('1' if res==1 else '')
            else:
                r.append(a[len(a)-1-c])
            c+=1

        return ''.join(r[::-1])

if __name__ == '__main__':
    print Solution().addBinary('111','1111')
    print Solution().addBinaryOld('111','1111')










