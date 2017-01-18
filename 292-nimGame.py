'''
292. Nim Game
Total Accepted: 43324 Total Submissions: 84870 Difficulty: Easy

You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

Hint:

    If there are 5 stones in the heap, could you figure out a way to remove the stones such that you will always be the winner?


    '''
class Solution(object):
    def canWinNim(self, n):
        return n%4!=0



    def canWinNimOld(self, n):
        """
        :type n: int
        :rtype: bool
        """

        '''


        fastest:
        return False if n%4 else True
        '''

        canWinList='111'
        known={'111':'0'}

        if n<=3:return canWinList[n-1]


        for i in xrange(3,n):
            if canWinList in known:
                canWinList=canWinList[1:]+known[canWinList]
            else:
                new=str(1-min(int(canWinList[0]),int(canWinList[1]),int(canWinList[2])))
                known[canWinList]=new
                canWinList=canWinList[1:]+new


        
        return bool(int(canWinList[-1]))


if __name__=='__main__':
    print Solution().canWinNim(4000000)