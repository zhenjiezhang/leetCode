'''
224. Basic Calculator
Total Accepted: 21952 Total Submissions: 106016 Difficulty: Medium

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:

"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23

Note: Do not use the eval built-in library function. 
'''
"""
this is not good for * or /. 
using recursion is better, but less elegent
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        values=[]
        ops=[1]
        sign=1

        result=0
        for elem  in self.extract(s):
            elem=elem.strip()

            if elem=='-':
                sign=-1
            elif elem=='+' or elem=='':
                sign=1
            elif elem=='(':
                ops.append(ops[-1]*sign)
                sign=1
            elif elem==')':
                ops.pop()
            else:
                result+=int(elem)*sign*ops[-1]
        return result

        
    def extract(self, s):
        head=tail=0
        while tail < len(s):
            while tail < len(s) and s[tail] not in {'+','-','(',')'}:
                tail+=1
            if tail==head:
                yield s[head]
                head+=1
                tail+=1
            else:
                yield s[head:tail]
                head=tail

if __name__ == '__main__':
    print Solution().calculate('6  +  7 -(9-(2-1))  ')




