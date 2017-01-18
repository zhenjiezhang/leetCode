'''273. Integer to English Words
Total Accepted: 11737 Total Submissions: 65635 Difficulty: Medium

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,

123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Hint:

    Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
    '''
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
        	return 'Zero'

        names=['','Thousand','Million','Billion']

        digits=['','One','Two','Three','Four','Five','Six','Seven',\
        'Eight','Nine']
        teens=['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen',\
        'Sixteen','Seventeen','Eighteen','Nineteen']
        tens=['Twenty','Thirty','Forty','Fifty','Sixty',\
        'Seventy','Eighty','Ninety']

        result=''
        if num<1000:
        	hundredDigit=num/100
        	if hundredDigit:
        		result+=digits[hundredDigit]+' '+'Hundred '
        	num=num%100
        	tenDigit=num/10
        	if tenDigit==1:
        		result+=teens[num%10]+' '
        	else:
        		result+=tens[tenDigit-2]+' ' if tenDigit>0 else ''
        		digit=num%10
        		result+=digits[num%10]+' ' if digit!=0 else ''
        	return result[:-1]


        for i in [3,2,1,0]:
        	seg=num/1000**i
        	num=num%(1000**i)

        	if seg:
        		result+=self.numberToWords(seg)\
        		+((' '+names[i]+' ') if i >0 else '')
        return result if result[-1] !=' ' else result[:-1]

if __name__=='__main__':
	s=Solution()
	print s.numberToWords(12345).replace(' ','.')
	print s.numberToWords(1000).replace(' ','.')
	print s.numberToWords(101).replace(' ','.')




        