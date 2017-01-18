'''
150. Evaluate Reverse Polish Notation
Total Accepted: 58197 Total Submissions: 256161 Difficulty: Medium

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6



Excellent thought!
  '''

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
    	stack=[]
    	ops=set(['+','-','*','/'])
    	for i in tokens:
    		if i not in ops:
    			stack.append(int(i))
    		else:
    			if i=='+':
    				stack.append(stack.pop()+stack.pop())
    			elif i=='-':
    				stack.append(-stack.pop()+stack.pop())
    			elif i=='*':
    				stack.append(stack.pop()*stack.pop())
    			elif i=='/':
    				p2=stack.pop()
    				p1=stack.pop()
                    # need to get integer as result
    				ans=abs(p1)/abs(p2)
    				ans=-ans if p1/p2<0 else ans
    				stack.append(ans)
    	return stack[0]

if __name__ == '__main__':
	solution=Solution()
	print solution.evalRPN(["4","-2","/","2","-3","-","-"])
