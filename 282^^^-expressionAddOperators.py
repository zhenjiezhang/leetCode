

'''
282. Expression Add Operators
Total Accepted: 7512 Total Submissions: 32545 Difficulty: Hard

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples:

"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []


'''




from time import time
class Solution(object):
    # slower, no caching
    def addOperators(self, nums, target):
        self.result=[]
        self.nums=nums
        self.target=target

        self.workingString=['',0,0]#current string, evaluation, last multiplication number
        for i in xrange(len(nums)):
            thisNum=int(nums[:i+1])
            self.workingString=[nums[:i+1], thisNum, thisNum]
            self.bfsDown(i+1)
        return self.result

    def bfsDown(self, start):
        if start==len(self.nums) and self.workingString[1]==self.target:
            self.result.append(self.workingString[0])

        for end in xrange(start+1, len(self.nums)+1):
            if self.nums[start]=='0' and end>start+1:
                break
            thisNumString=self.nums[start:end]
            thisNum=int(thisNumString)

            oldString=self.workingString
            self.workingString=[oldString[0]+'+'+thisNumString, oldString[1]+thisNum, thisNum]
            self.bfsDown(end)
            self.workingString=[oldString[0]+'-'+thisNumString, oldString[1]-thisNum, thisNum]
            self.bfsDown(end)
            self.workingString=[oldString[0]+'*'+thisNumString, oldString[1]-oldString[2]+oldString[2]*thisNum, oldString[2]*thisNum]
            self.bfsDown(end)






    def addOperatorsBackTrack(self, nums, target):
        if not nums:
            return []
        self.cache=dict()
        self.nums=nums
        return [l[2] for l in self.bfs(0) if l[1]==target]


    def bfs(self, start):
        if start in self.cache:
            return self.cache[start]
        if start==len(self.nums)-1:
            thisNum=int(self.nums[-1])
            return [[thisNum, thisNum, self.nums[-1]]]

        thisNum=int(self.nums[start:])
        cur=[[thisNum, thisNum, self.nums[start:]]] if self.nums[start]!='0' else []

        for i in xrange(start+1, len(self.nums)):
            if self.nums[start]=='0' and i>start+1:
                break
            thisNumString=self.nums[start: i]
            thisNum=int(thisNumString)
            next=self.bfs(i)
            cur.extend([[thisNum, thisNum+l[1], thisNumString+'+'+l[2]] for l in next])
            cur.extend([[thisNum, thisNum+l[1]-2*l[0], thisNumString+'-'+l[2]] for l in next])
            cur.extend([[thisNum*l[0], thisNum*l[0]+l[1]-l[0], thisNumString+'*'+l[2]] for l in next])
        self.cache[start]=cur
        return cur






    def addOperatorsOld(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        result=[]
        if num and int(num)==target and not(len(num)>1 and num[0]=='0'):
            # result.append(num)
            result.append(num)
        for i in xrange(len(num)-1,0,-1):
            if len(num)-i>1 and num[i]=='0':
                continue

            plus=self.addOperators(num[:i], target-int(num[i:]))
            for e in plus:
                result.append(e+'+'+num[i:])

            minus=self.addOperators(num[:i],target+int(num[i:]))
            for e in minus:
                result.append(e+'-'+num[i:])

            for j in xrange(i-1,-1,-1):
                if i-j>1 and num[j]=='0':
                    continue
                tmp=self.operatorsWithLastNum(num[:j], int(num[j:i])*int(num[i:]), target)
                if tmp:
                    result+=[e+num[j:i]+'*'+num[i:] for e in tmp]
        return result



    def operatorsWithLastNum(self, num, last, target):
        result=[]
        if not num:
            return result if last!=target else ['']

        plus=self.addOperators(num,target-last)
        if plus:
            result+=[e+'+' for e in plus]
        minus=self.addOperators(num,target+last)
        if minus:
            result+=[e+'-' for e in minus]


        for i in xrange(len(num)-1,-1,-1):
            if len(num)-i>1 and num[i]=='0':
                continue
            newLast=int(num[i:])
            times=self.operatorsWithLastNum(num[:i], newLast*last,target)
            if times:
                result+=[e+str(newLast)+'*' for e in times]
        return result








if __name__=='__main__':
    print Solution().addOperators("105", 5)

    t1=time()
    print Solution().addOperators("105", 5)
    print Solution().addOperators("00", 0)
    print Solution().addOperators("232", 8)
    print Solution().addOperators("123", 6)
    for i in xrange(12):
        len(Solution().addOperators("123456789", 45))
    print time()-t1

    t1=time()

    print Solution().addOperatorsOld("105", 5)
    print Solution().addOperatorsOld("00", 0)
    print Solution().addOperatorsOld("232", 8)
    print Solution().addOperatorsOld("123", 6)
    for i in xrange(12):
        len(Solution().addOperatorsOld("123456789", 45))
    print time()-t1







        