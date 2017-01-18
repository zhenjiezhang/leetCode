'''# The read4 API is already defined for you.
157. Read N Characters Given Read4
Total Accepted: 8446 Total Submissions: 28904 Difficulty: Easy

The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function will only be called once for each test case. 


'''

# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):
        num=0
        buffer=[""]*4
        
        thisRead=read4(buffer)
        while thisRead>0:
            num+=thisRead
            buf[num-thisRead:min(n, num)]=buffer[:thisRead]
            if n<=num:
                return n
            thisRead=read4(buffer)
        return num