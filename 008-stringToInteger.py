class Solution:
    # @return an integer
    def atoi(self, string):
        string=string.strip()
        digits=set([str(i) for i in xrange(10)])
        result=0
        if string and string[0] in {'+','-','.'}|digits:

            sign=-1 if string[0]=='-' else 1

            if string[0] in {'+','-'}:
                string=string[1:]
            string=string.lstrip('0')

            i=0
            while i<len(string) and string[i] in digits:
                result=result*10+int(string[i])
                i+=1

            if i<len(string) and string[i]=='.':
                string=string.rstrip('0')
                i+=1
                p=1
                while i<len(string) and string[i] in digits:
                    result+=float(string[i])/10**p
                    p+=1
                    i+=1
        else:
            return 0

        result=result*sign
        if result > 2147483647:
            return 2147483647
        elif result<-2147483648:
            return -2147483648
        else:
            return result

print Solution().atoi('-032.090')



