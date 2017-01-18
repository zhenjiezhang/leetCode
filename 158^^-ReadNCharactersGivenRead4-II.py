'''
158. Read N Characters Given Read4 II - Call multiple times
Total Accepted: 6785 Total Submissions: 29420 Difficulty: Hard

The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file. 

'''

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def __init__(self):
        self.leftOver=['a','b']
        self.buffer=[""]*4

    def read(self, buf, n):
        if len(self.leftOver)>=n:
            # deadly important to use buf[:] instead of buf!!!!!!!!!!!!!!
            buf[:]=self.leftOver[:n]

            self.leftOver=self.leftOver[n:]
            return n
        
        buf[:len(self.leftOver)]=self.leftOver
        num=len(self.leftOver)

        thisRead=read4(self.buffer)
        while thisRead>0:
            num+=thisRead
            buf[num-thisRead:min(n, num)]=self.buffer[:thisRead+n-num]
            if n<=num:
                self.leftOver=self.buffer[thisRead+n-num:thisRead]
                return n
            thisRead=read4(self.buffer)

        return num


if __name__=="__main__":
    solution=Solution()
    a=['']
    solution.read(a,1)
    print a
    print solution.leftOver