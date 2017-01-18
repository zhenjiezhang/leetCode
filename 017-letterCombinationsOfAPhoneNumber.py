class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if not digits:
            return []
        results,alphabets=[''],[' ','1','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        for i in digits:
            results=[s+c for s in results for c in alphabets[int(i)]]
        return results

if __name__=="__main__":

    solution=Solution()
    print solution.letterCombinations('23')
