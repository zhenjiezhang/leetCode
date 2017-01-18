# you can directly code 'CM', 'CD', 'XC', 'XL', 'IX' and 'IV' in the dict.

class Solution:
    # @return an integer
    def romanToInt(self, s):
        convertDict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500, 'M':1000}
        i=0
        result=0
        while i < len(s):
            curNum=convertDict[s[i]]
            if i+1<len(s):
                nextNum=convertDict[s[i+1]]
                if curNum < nextNum:
                    curNum=nextNum-curNum
                    i+=1
            result+=curNum
            i+=1
        return result


solution=Solution()
print solution.romanToInt('XCIX')




