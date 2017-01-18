class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float

    #bit is faster
    def myPow(self, x, n):
        result=1
        power=abs(n)

        digit=0
        while digit<=32:
            while digit <=32 and not (power>>digit)&1:
                digit+=1

            if digit>32:
                break

            xPower=x
            for _ in xrange(digit):
                xPower*=xPower

            result*=xPower

            digit+=1

        return result if n>=0 else 1.0/result




    def myPowOld(self, x, n):
        
        res=abs(n)
        result=1
        while(res>0):
            power=1
            while (2**power<=res):
                power+=1
            xPower=x
            for i in xrange(power-1):
                xPower=xPower*xPower
            result*=xPower
            # print result, x, res
            res-=2**(power-1)
        return result if n>=0 else 1.0/result

solution=Solution()
print solution.myPow(6,3)
print solution.myPow(34,-3)



