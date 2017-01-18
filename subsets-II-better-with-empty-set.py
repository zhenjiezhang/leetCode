class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        if not S:
            return [[]]

        S.sort()
        result=[[]]

        for i in range(len(S)):
            addpart=[]
            if i>0 and S[i]==S[i-1]:
                for item in oldresult:
                    add=item[:]
                    add.append(S[i])
                    addpart.append(add)
            else:
                for item in result:
                    add=item[:]
                    add.append(S[i])
                    addpart.append(add)

            oldresult=addpart

            result.extend(addpart)


        return result

if __name__ == '__main__':
    solution=Solution()
    print solution.subsetsWithDup([1,1,2,2,2])