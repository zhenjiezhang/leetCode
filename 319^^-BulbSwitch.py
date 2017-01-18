'''
319. Bulb Switcher
Total Accepted: 10367 Total Submissions: 26248 Difficulty: Medium

There are n bulbs that are initially off. You first turn on all the bulbs. 
Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). 
For the nth round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Given n = 3. 

At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.




my post:
https://leetcode.com/discuss/86778/explanation-for-the-square-root-method
For any light, say, light k, it only gets switched when the interval is a factor of k. Now, notice that factors come in pairs, that is, if a*b==k, you will switch light k at both intervals a and b. As long as a !=b, the light k will be off in the end. The only chance that light k remains on is when a==b, that is, k==a^2, , in this case it only gets switched once for this pair of factors. So, k needs to be a square number!

Then the question is really asking how many square numbers are smaller or equal to N, which is trivial to programmers.


faster than using sqrt
'''
from math import sqrt
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """

        '''
        this did not speed things up... 
        '''

        k=n
        counter=0
        while k:
            counter+=1
            k=k>>1
        k=(1<<counter/2)/2

        # print n, ':', k

        '''
        rather use k=1
        '''

        k=1

        while k**2 <=n:
            k+=1

        return k-1

if __name__ == '__main__':
    solution=Solution()
    for i in xrange(100):
        print i, solution.bulbSwitch(i), int(sqrt(i))