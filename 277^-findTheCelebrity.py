'''
277. Find the Celebrity
Total Accepted: 5430 Total Submissions: 15513 Difficulty: Medium

Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1. 
'''

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        knownTable=[
        [1,1,1,1,0,0],
        [0,1,0,1,0,0],
        [0,0,1,1,0,0],
        [1,1,0,1,0,0],
        [0,0,0,1,1,0],
        [0,0,0,1,1,1]
        ]
        
        def knows(a,b):
            return bool(knownTable[a][b])

        questioner=reduce(lambda x, y: y if knows(x,y) else x, xrange(n))

        for p in xrange(questioner):
            if knows(questioner, p) or not knows(p, questioner):
                return -1
        for p in xrange(questioner+1, n):
            if not knows(p, questioner):
                return -1
        return questioner



if __name__ == '__main__':
    print Solution().findCelebrity(6)





