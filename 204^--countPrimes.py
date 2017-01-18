'''
204. Count Primes
Total Accepted: 49654 Total Submissions: 215208 Difficulty: Easy

Description:

Count the number of prime numbers less than a non-negative number, n.


\

this is an optimization:

publib int countPrimes(int n) {
    if (n < 3)
        return 0;

    boolean[] f = new boolean[n];
    //Arrays.fill(f, true); boolean[] are initialed as false by default
    int count = n / 2;
    for (int i = 3; i * i < n; i += 2) {
        if (f[i])
            continue;

        for (int j = i * i; j < n; j += 2 * i) {
            if (!f[j]) {
                --count;
                f[j] = true;
            }
        }
    }
    return count;
}
'''

class Solution(object):
    def countPrimes_tooSlow(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes=[]

        if n<2:
            return 0

        for i in range(2,n+1):
            iIsPrime=True
            for p in primes:
                if p > i**0.5:
                    break
                if i%p==0:
                    iIsPrime=False
                    break
            if iIsPrime:
                primes.append(i)
        return len(primes)

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=2:
            return 0
        remaining=[1 for _ in xrange(n)]

        limit=int(n**.5)

        for i in xrange(2, limit+1):
            if remaining[i]==1:
                for m in xrange(i*i, n,i):
                    remaining[m]=0
        return sum(remaining)-2




if __name__ == '__main__':
    print Solution().countPrimes(1500000)
