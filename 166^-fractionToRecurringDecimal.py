'''
166. Fraction to Recurring Decimal
Total Accepted: 25391 Total Submissions: 176484 Difficulty: Medium

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

    Given numerator = 1, denominator = 2, return "0.5".
    Given numerator = 2, denominator = 1, return "2".
    Given numerator = 2, denominator = 3, return "0.(6)".

    '''
class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if numerator==0:
            return '0'

        sign=-1 if (numerator<0)^(denominator<0) else 1
        numerator,denominator=abs(numerator),abs(denominator)

        result=[numerator/denominator]
        residue=numerator%denominator
        residueHistory={}
        i=1
        while residue!=0:
            if residue in residueHistory:
                start=residueHistory[residue]
                return ('-' if sign==-1 else '')+str(result[0])+'.'+''.join([str(result[r]) for r in xrange(1, start)])+\
'('+''.join([str(result[r]) for r in xrange(start,len(result))])+')'

            residueHistory[residue]=i
            residue*=10
            result.append(residue/denominator)
            residue%=denominator
            i+=1

        return ('-' if sign==-1 else '')+str(result[0])+(('.'+''.join([str(result[r]) for r in xrange(1, len(result))])) if len(result)>1 else '')




    def fractionToDecimalOld(self, numerator, denominator):
        if numerator==0:
            return '0'

        sign=-1 if (numerator<0)^(denominator<0) else 1
        numerator,denominator=abs(numerator),abs(denominator)


        ans=('0' if sign==1 else '-0') if numerator<denominator else (str(numerator/denominator) if sign==1 else '-'+str(numerator/denominator))
        previousRes=dict()

        res=numerator%denominator
        if res==0:
            return ans
        else:
            ans+='.'

        while res>0:
            if res in previousRes:
                repStart=previousRes[res]
                return ans[:repStart]+'('+ans[repStart:]+')'

            previousRes[res]=len(ans)
            res*=10
            while res<denominator:
                ans+='0'

                if res in previousRes:
                    repStart=previousRes[res]
                    return ans[:repStart]+'('+ans[repStart:]+')'

                previousRes[res]=len(ans)
                
                res*=10
                

            ans+=str(res/denominator)
            res=res%denominator
        return ans

if __name__ == '__main__':
    solution=Solution()
    print solution.fractionToDecimal(2,7)
    print solution.fractionToDecimal(1,90)
    print solution.fractionToDecimal(8,4)



