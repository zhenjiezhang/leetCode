'''
9. Palindrome Number
Total Accepted: 98534 Total Submissions: 325897 Difficulty: Easy

Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.
Some hints:

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''




class Solution:
    # @return a boolean
    def isPalindrome(self, x):
    	if x<0:
    		return False
    	digits=1
    	while x/10**digits!=0:
    		digits+=1
    	# print digits

    	for i in xrange(1,digits/2+1):
    		# print x%10**i/10**(i-1)
    		if x%10**i/10**(i-1)!=x%10**(digits+1-i)/10**(digits-i):
    			return False
    	return True

print Solution().isPalindrome(0144410)
        