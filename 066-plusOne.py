'''
66. Plus One
Total Accepted: 80472 Total Submissions: 250395 Difficulty: Easy

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        digits=digits[::-1]+[0]
        i=0
        while i <len(digits):
        	digits[i]+=1
        	if digits[i]==10:
        		digits[i]=0
        		i+=1
        	else:
        		break
        return digits[::-1] if digits[-1]==1 else digits[-2::-1]

if __name__ == '__main__':
	print Solution().plusOne([])


