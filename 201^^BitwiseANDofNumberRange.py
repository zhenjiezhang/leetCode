'''
201. Bitwise AND of Numbers Range
Total Accepted: 27683 Total Submissions: 95737 Difficulty: Medium

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4. 










this is a lot more straight forward than mine....

def rangeBitwiseAnd(self, m, n):
    i = 0
    while m != n:
        m >>= 1
        n >>= 1
        i += 1
    return n << i
'''

class Solution(object):
    # you only need to take care of the identical bit of m and n, before the first different bit. Use xor to find out the first different bit, 
    # and make a mask out of it, to mask out he identical bits before that different bit.
    def rangeBitwiseAnd(self, m, n):
        xor=m^n

        mask=0
        i=0
        while xor:
            mask+=1<<i
            i+=1
            xor>>=1

        mask=~mask
        return m&mask



    import math
    def rangeBitwiseAndOld(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==0:
            return 0
        m_op,n_op=m,n
        high_m=int(math.log(m_op,2))
        high_n=int(math.log(n_op,2))

        result=0

        while high_n==high_m:
            high_order=2**high_n

            result+=high_order
            m_op-=high_order
            n_op-=high_order
            if m_op==0:
                return result
            high_m=int(math.log(m_op,2))
            high_n=int(math.log(n_op,2))
        return result

if __name__=="__main__":

    solution=Solution()

    print solution.rangeBitwiseAnd(5,7)
    print solution.rangeBitwiseAndOld(5,7)

    print solution.rangeBitwiseAnd(1,1)



