'''
72. Edit Distance
Total Accepted: 50209 Total Submissions: 181459 Difficulty: Hard

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
'''

'''
A better solution:

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        dist = range(len(word2) + 1)
        for i in xrange(len(word1)):
            dist_ij, dist[0] = i, i + 1
            for j in xrange(len(word2)):
                if word1[i] == word2[j]:
                    dist_ij, dist[j + 1] = dist[j + 1], dist_ij
                else:
                    dist_ij, dist[j + 1] = dist[j + 1], min(dist[j], dist[j + 1], dist_ij) + 1
        return dist[-1]

my analysis:
This is better than my solution which uses a 3-way min comparison each time. 
This algorithm saves time when word1[i]==word2[j] by directly matching the latest letters.
 I will attempt to elaborate the reasoning as following, as a reinforcement for myself (better if it actually helps someone else: ):

When word1[i]==word2[j], let's say, the letter is m, if in the best alignment of [i,j], 
word1[i] does not align with word2[j], that is, alignment[ij]==alignment[i][j-1]+1 or alignment[i-1][j]+1,
let's see what happens.

Since word1[i] and word2[j] are both m, and word1[i] does not align with word2[j], then before word2[j] comes into play, 
the m of word[i] must have aligned with some other m in word2. Why is this the case? Suppose if it is not the case,
 that is, word1[i] is not aligned with a m in word2, before word2[j] comes in, then, it would mean that, 
 word1[i] is free to marry with word2[j] at no cost, since it is the last letter at this stage, 
 that would make the alignment of word1[:i], word2[:j] identical to word1[:i], word2[:j-1], 
 which is certainly better than the match of [i,j-1]+1. 
 Well, now, we know that word1[i] is aligned with some m in word2 before word2[j]. 
 Well, since that would mean that, if word1[i] does not align with word2[j], 
 then all letters after that earlier m in word2 would be insertions. 
 In this case, if we re-marry word1[i] to word2[j], nothing would change in alignment score. 
 So, we have proved that we can always make the score better than alignment[i,j-1]+1, 
 let's take care of the case of alignment[i-1, j]+1. 
 But wait, we are dealing with a symmetric problem, word1 and word2 are symmetric in playing the rules, 
 and the analysis is necessarily identical for the case of alignment[i-1, j] and alignment[i, j-1] when compared to alignment[i,j]. 
 The fact that we are working in growing word2 first or word1 first does not affect the analysis since we are not relying on it. 
 So, we have proved that when word1[i]==word2[j], then if we marry the two, 
 the alignment score will be at least as good as alignment[i-1, j] and alignment[i, j-1], 
 which is certainly better than either of them plus 1. So, we do not have to consider the plus one cases,
  but just need to directly jump to alignment[i-1][j-1].

'''

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
    	trackTable=[[0]*(len(word2)+1) for _ in range (len(word1)+1)]
    	for j in range (len(word2)+1):
    		trackTable[0][j]=j
        for i in range (1, len(word1)+1):
            trackTable [i][0]=i

    	for i in range(1,len(word1)+1):
    		# letter=word1[i-1]
    		for j in range(1,len(word2)+1):
    			trackTable[i][j]=min(trackTable[i][j-1]+1,trackTable[i-1][j]+1,trackTable[i-1][j-1]+\
                 (0 if word1[i-1]==word2[j-1] else 1))

    	return trackTable[len(word1)][len(word2)]

if __name__=="__main__":
	solution=Solution()
	print solution.minDistance("attg","atctgggg")
	print solution.minDistance("","")



