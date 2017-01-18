'''
179. Largest Number
Total Accepted: 38044 Total Submissions: 211935 Difficulty: Medium

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''




'''
Proof:

    Let us define f(X) = 10^(lgX + 1), then XY = f(Y)X + Y

    If AB <= BA, then we have
    f(B)A + B <= f(A)B + A
    (f(B) - 1)A <= (f(A) - 1)B
    that is
    A <= B·(f(A) - 1) / (f(B) - 1)   (1)

    If BC <= CB, then we have
    f(C)B + C <= f(B)C + B
    (f(C) - 1)B <= (f(B) - 1)C
    that is
    B <= C·(f(B) - 1) / (f(C) - 1)   (2)

    Combine (1), (2), we have
    A <= C·(f(A) - 1) / (f(C) - 1)
    (f(C) - 1)A <= (f(A) - 1)C
    f(C)A + C <= f(A)C + A
    AC <= CA

    '''
class Solution:
    # @param num, a list of integers
    # @return a string
    
    def compare(self, n1,n2):
        n1=str(n1)
        n2=str(n2)
        if int(n1+n2)<int(n2+n1):
            return 1
        elif int(n1+n2)>int(n2+n1):
            return -1
        else:
            return 0





    def largestNumber(self, num):
   

        num=sorted(num,cmp=self.compare)
        result=(''.join([str(n) for n in num]))
        if result[0]=='0':
            return '0'
        else:
            return result



print Solution().largestNumber([0,0,2])

