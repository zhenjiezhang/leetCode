'''
299. Bulls and Cows
Total Accepted: 18383 Total Submissions: 64755 Difficulty: Easy

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

For example:

Secret number:  "1807"
Friend's guess: "7810"

Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. In the above example, your function should return "1A3B".

Please note that both secret number and friend's guess may contain duplicate digits, for example:

Secret number:  "1123"
Friend's guess: "0111"

In this case, the 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow, and your function should return "1A1B".

You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
'''
from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        bull=sum([1 for a,b in zip(secret, guess) if a==b])
        cs=Counter([a for a,b in zip(secret, guess) if a!=b])
        cg=Counter([b for a,b in zip(secret, guess) if a!=b])
        keys=set(cs.keys()) & set(cg.keys())
        return `bull`+'A'+`sum([min(cs[k],cg[k]) for k in keys])`+'B'



    def getHintOld(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        b=0
        c=0
        cDict={}
        for i in xrange(len(secret)):
            if secret[i]==guess[i]:
                b+=1
            else:
                if secret[i] in cDict:
                    cDict[secret[i]]+=1
                else:
                    cDict[secret[i]]=1

        for i in xrange(len(guess)):
            if guess[i]!=secret[i] and guess[i] in cDict and cDict[guess[i]]!=0:
                c+=1
                cDict[guess[i]]-=1

        return str(b)+'A'+str(c)+'B'


if __name__ == '__main__':
    print Solution().getHint('1807','7810')