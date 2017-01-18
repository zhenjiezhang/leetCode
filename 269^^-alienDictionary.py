'''
269. Alien Dictionary
Total Accepted: 5081 Total Submissions: 23604 Difficulty: Hard

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

For example,
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

The correct order is: "wertf".




Better code than mine!

def alienOrder(self, words):
    less = []
    for pair in zip(words, words[1:]):
        for a, b in zip(*pair):
            if a != b:
                less += a + b,
                break
    chars = set(''.join(words))
    order = []
    while less:
        free = chars - set(zip(*less)[1])
        if not free:
            return ''
        order += free
        less = filter(free.isdisjoint, less)
        chars -= free
    return ''.join(order + list(chars))
'''

class Solution(object):
    def alienOrder(self, words):

        if not words:
            return ''

        result=[]
        allLettters=set([l for w in words for l in w])
        secondToTable={l: set() for l in allLettters}

        pairs=zip(words, words[1:])
        for p in pairs:
            for l1, l2 in zip(*p):
                if l1!=l2:
                    secondToTable[l2].add(l1)
                    break
                    
        while allLettters:
            headLetter=''

            for l in allLettters:

                if not secondToTable[l]:

                    headLetter=l
                    break
            if not headLetter:
                return ''
            allLettters.remove(headLetter)

            for l in secondToTable:
                if headLetter in secondToTable[l]:
                    secondToTable[l].remove(headLetter)

            result.append(headLetter)

        return ''.join(result)


if __name__ == '__main__':
    solution=Solution()
    print solution.alienOrder(["za","zb","ca","cb"])
    print solution.alienOrder(["wrt","wrf","er","ett","rftt"])
#     print solution.alienOrder(
#         [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ])
