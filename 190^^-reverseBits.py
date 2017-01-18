'''
190. Reverse Bits
Total Accepted: 50726 Total Submissions: 173920 Difficulty: Easy

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it? 



private int[] reverseHex = new int[] {0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15};

// you need treat n as an unsigned value
public int reverseBits(int n) {
    int rev = 0;
    while (n != 0) {
        rev = (rev << 4) + reverseHex[n & 0xF];
        n >>>= 4;
    }
    return rev;
}

    Create an array that contains the reverse number of 0-15.
    Divide the number into 8 parts, each part has 4 bits which can represent number 0-15. Get the reverse number of each part using the array.


'''
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        result=0
        for _ in xrange(32):
            # << and & have low priority
            result=(result<<1)+(n&1)
            # print result
            n>>=1
        return result


    def reverseBitsOld(self, n):
        result=0
        for i in xrange(32):
        	b=1<<i
        	if i<=15:
        		result+=(n&b)<<(31-2*i)
        	else:
        		result+=(n&b)>>(2*i-31)
        return result

print Solution().reverseBits(43261596)
print Solution().reverseBitsOld(43261596)
