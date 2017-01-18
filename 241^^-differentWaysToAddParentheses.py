class Solution(object):
    def __init__(self):
        self.ops={'+':lambda x,y:x+y, '-':lambda x,y:x-y, '*': lambda x,y:x*y}
        self.cache=dict()
        '''
        could use dynamic programming too.
        '''

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input in self.cache:
            return self.cache[input]

        result=[]
        for i in xrange(len(input)):
            if input[i] in '+-*':
                l=self.diffWaysToCompute(input[:i])
                r=self.diffWaysToCompute(input[i+1:])
                result+=[self.ops[input[i]](x,y)\
                 for x in l for y in r]

        result=result if result else [int(input)]
        self.cache[input]=result
        return result

if __name__=='__main__':
    print Solution().diffWaysToCompute('1-2*3+1')

