"""
a faster version, basically the same to mine, but there are some nice implementing tricks

def calculate(self, s):
    s = s + "+"  # guard
    res, num, sign, stack = 0, 0, 1, []
    for ss in s:
        if ss.isdigit(): # deal with numbers
            num = 10*num + ord(ss)-ord("0") # faster than int(ss)
        elif ss in "+-":
            if stack and stack[-1] in "*/": # update number in a "*/" expression
                md, val = stack.pop(), stack.pop()
                num = val*num if md == "*" else val/num
            res, num, sign = res + sign*num, 0, [-1, 1][ss=="+"]
        elif ss in "*/":
            if stack and stack[-1] in "*/": # update number in a "*/" expression
                md, val = stack.pop(), stack.pop()
                num = val*num if md == "*" else val/num
            stack.extend([num, ss]) # if no previous "*/", append directly
            num = 0
    return res
"""


"""
my version
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        values=[]
        ops=[]

        for t in self.extract(s):
            t=t.strip()
            if t=='+' or t=='-':
                while len(ops)>0:
                    op=ops.pop()
                    right=values.pop()
                    left=values.pop()
                    if op=='+':
                        r=left+right
                    elif op=='-':
                        r=left-right
                    values.append(r)
                ops.append(t)

            elif t=='*' or t=='/':
                ops.append(t)   

            elif t=='':
                pass

            else:
                v=int(t)
                if len(ops)>0:
                    op=ops.pop()
                    if op=='*':
                        v*=values.pop()
                    elif op=='/':
                        v=values.pop()/v
                    else:
                        ops.append(op)
                values.append(v)


        while len(ops)>0:
            op=ops.pop()
            right=values.pop()
            left=values.pop()
            r=0
            if op=='+':
                r=left+right
            elif op=='-':
                r=left-right
            values.append(r)
        return values[0]







    def extract(self, s):
        head=tail=0
        while tail < len(s):
            while tail < len(s) and s[tail] not in {'+','-','/','*'}:
                tail+=1
            if tail==head:
                yield s[head]
                head+=1
                tail+=1
            else:
                yield s[head:tail]
                head=tail
if __name__ == '__main__':
    s=Solution()
    print s.calculate('3+2*2/3-  8/3-5*2*2 ')