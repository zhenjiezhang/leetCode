'''
294. Flip Game II
Total Accepted: 5978 Total Submissions: 14823 Difficulty: Medium

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity. 
read this to speed up!
https://leetcode.com/discuss/64344/theory-matters-from-backtracking-128ms-to-dp-0ms
'''

class Solution(object):

    def canWin(self, s):
        pluses=re.split('-+',s)
        win=0
        for p in pluses:




    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.buffer={}
        return self.win(s)



    def win(self, s):
        


        afterOneStep=self.generatePossibleNextMoves(s)
        if s in self.buffer:
            return self.buffer[s]

        if not afterOneStep:
            self.buffer[s]=False
            return False

        for ss in afterOneStep:
            if not self.win(ss):
                self.buffer[s]=True
                return True

        self.buffer[s]=False

        return  False


    
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        indexes=filter(lambda i: s[i:i+2]=='++', xrange(len(s)-1))
        return [s[:i]+'--' +s[i+2:] for i in indexes]

if __name__ == '__main__':
    solution=Solution()
    for i in xrange(44):
        print i, solution.canWin('+'*i)
