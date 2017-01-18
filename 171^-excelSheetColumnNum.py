'''
171. Excel Sheet Column Number
Total Accepted: 61792 Total Submissions: 154746 Difficulty: Easy

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A to 1
    B to 2
    C to 3
    ...
    Z to 26
    AA to 27
    AB to 28 
    '''
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        number=0
        base=26
        for i in xrange(len(s)-1):
            number+=base
            base*=26

        base=26**(len(s)-1)
        for i in xrange(len(s)):
            number+=(ord(s[i])-65)*base
            base/=26
            
        return number+1

if __name__ == '__main__':
    print Solution().titleToNumber('AB'), 28




        