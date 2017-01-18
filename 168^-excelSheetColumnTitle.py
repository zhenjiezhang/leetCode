'''
168. Excel Sheet Column Title
Total Accepted: 49824 Total Submissions: 243424 Difficulty: Easy

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 to A
    2 to B
    3 to C
    ...
    26 to Z
    27 to AA
    28 to AB 
    '''
class Solution:
    # @return a string
    def convertToTitle(self, num):
        highPlace=1

        base=26
        while num>base:
            num-=base
            base*=26
            highPlace+=1


        result=''
        base=26**highPlace
        for i in xrange(highPlace-1,0,-1):
            base/=26
            r=(num)/base
            # because excel number is 1 based, special cases need to be taken care of:  进位在前一位的未尾，而不是后一位的开头
            if (num)%base==0:
                return result+chr(r+64)+'Z'*i
            else:
                result+=chr(r+65)
            num-=(r)*26**i
        result+=chr(num+64)
        return result

if __name__ == '__main__':
    print Solution().convertToTitle(26**3+26*26+26)
    print Solution().convertToTitle(27)

    # print Solution().convertToTitle(27)

        