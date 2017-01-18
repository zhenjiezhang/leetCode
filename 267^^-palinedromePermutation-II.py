'''
267. Palindrome Permutation II
Total Accepted: 3642 Total Submissions: 13719 Difficulty: Medium

Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

For example:

Given s = "aabb", return ["abba", "baab"].

Given s = "abc", return [].

Hint:

    If a palindromic permutation exists, we just need to generate the first half of the string.
    To generate all distinct permutations of a (half of) string, use a similar approach from: Permutations II or Next Permutation.

    '''
class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        letterCount=[0]*128
        center=''


        for c in s:
            letterCount[ord(c)]+=1

        for i in xrange(128):
            if letterCount[i]%2==1:
                if not center:
                    center=chr(i)
                else:
                    return []

            letterCount[i]//=2


        letters={i for i in xrange(128) if letterCount[i]>0}
        if not len(letters):
            return [center]


        results=self.generate(letterCount, letters)

        for l in xrange(len(results)):
            results[l]=[chr(i) for i in results[l]]

        results=[''.join(s) for s in results]
        return [center.join([s, s[::-1]]) for s in results]


    def generate(self, letterCount, letters):

        if len(letters)==1:
            l=letters.pop()
            letters.add(l)
            return [[l]*letterCount[l]]

        results=[]

        for l in letters:
            letterCount[l]-=1
            if letterCount[l]==0:
                letters.remove(l)

            for s in self.generate(letterCount, letters):
                results.append([l])
                results[-1].extend(s)


            if letterCount[l]==0:
                letters.add(l)
            letterCount[l]+=1
        return results

if __name__ == '__main__':
    solution=Solution()
    print solution.generatePalindromes('aab')
    print solution.generatePalindromes('a')


