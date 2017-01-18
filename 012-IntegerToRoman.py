class Solution:
    # @return a string
    def intToRoman(self, num):

        Roman=''
        RomanNumbers=[[1000,'M'],
                      [500,'D'],
                      [100,'C'],
                      [50,'L'],
                      [10,'X'],
                      [5,'V'],
                      [1,'I']]

        for r in xrange(0,len(RomanNumbers),2):
            if num>=RomanNumbers[r][0]:
                x=num/RomanNumbers[r][0]
                if x==9:
                    Roman+=RomanNumbers[r][1]+RomanNumbers[r-2][1]
                elif x==4:
                	Roman+=RomanNumbers[r][1]+RomanNumbers[r-1][1]
                elif x>=5:
                    Roman+=RomanNumbers[r-1][1]
                    for i in xrange(x-5):
                        Roman+=RomanNumbers[r][1]
                else:
	                for i in xrange(x):
	                    Roman+=RomanNumbers[r][1]
                num%=RomanNumbers[r][0]
        return Roman


if __name__=="__main__":
    solution=Solution()
    print solution.intToRoman(3940)
    print solution.intToRoman(9)
    print solution.intToRoman(44)
    print solution.intToRoman(54)
    print solution.intToRoman(4)

