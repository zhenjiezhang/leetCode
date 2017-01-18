'''
6. ZigZag Conversion
Total Accepted: 70152 Total Submissions: 308558 Difficulty: Easy

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". 

more lines like this:

a i q
bhjpr
cgko
dfln
e m

'''
# my original method, heavy math

class Solution:
    # @return a string
    def convertOld(self, s, nRows):

        if len(s)<nRows or nRows==1:
            return s

        zigSize=nRows*2-2
        zigNum=len(s)/zigSize
        hangover=len(s)%zigSize
        secHang=hangover-nRows if hangover > nRows else 0

        result=[]
        for i in xrange(nRows):
            for j in xrange(zigNum):
                result.extend([s[zigSize*j+i], (s[zigSize*(j+1)-i] if (i!=0 and i!=nRows-1) else '')])
            if i < hangover:
                result.append(s[zigSize*zigNum+i])
                if i >=nRows-1-secHang and i < nRows-1:
                    result.append(s[len(s)-1-secHang+nRows-1-i])
        return ''.join(result)
    #
    # same speed to old, but simple and nice: map letters to positions, instead of postions to letters!
    def convertNew(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        rows = [''] * numRows
        num = (numRows-1)*2
        for i, item in enumerate(s):
            if i % num >= numRows:
                rows[(num - i % num) % numRows] += item
            else:
                rows[i % num] += item
        return ''.join(rows)




    # table way:
    # but 10 times slower
    def convert(self, s, nRows):
        import numpy as np

        if len(s)<nRows or nRows==1:
            return s
        s=[ord(c) for c in s]
        zigSize=nRows*2-2
        zigNum=len(s)/zigSize+1
        table=np.array([[-1]*zigNum*2 for _ in xrange(nRows)])

        for i in xrange(zigNum-1):
            table[:,2*i]=s[zigSize*i: zigSize*i+nRows]
            table[1:nRows-1, 2*i+1]=s[zigSize*i+nRows: zigSize*(i+1)][::-1]
        hangover=len(s)%zigSize
        if hangover<=nRows:
            table[:hangover,2*zigNum-2]=s[zigSize*(zigNum-1): zigSize*(zigNum-1)+hangover]
        else:
            table[:,-2]=s[zigSize*(zigNum-1): zigSize*(zigNum-1)+nRows]
            table[-(hangover-nRows)-1:-1,-1]=s[-(hangover-nRows):][::-1]
        return ''.join([chr(table[i,j]) for i in xrange(len(table)) for j in xrange(len(table[0])) if table[i,j]!=-1])








if __name__=="__main__":
    import time
    solution=Solution()
    time1=time.time()
    for _ in xrange(1000): solution.convertOld("PAYPALISHIRING",5)
    time2=time.time()
    print time2-time1
    for _ in xrange(1000): solution.convert("PAYPALISHIRING",5)
    print time.time()-time2


    # print solution.convert("PA",3)
    # print solution.convert("ABC",2)
    # print solution.convert("ABC",3)
    # print solution.convert("ABCDE",4)


            

