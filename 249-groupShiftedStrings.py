'''
249. Group Shifted Strings
Total Accepted: 5908 Total Submissions: 19335 Difficulty: Easy

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"

Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Return:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

Note: For the return value, each inner list's elements must follow the lexicographic order.
'''


class Solution(object):
    def groupStrings(self, strings):
        allGroups=dict()
        for ss in strings:
            dis=ord(ss[0])-ord('a')
            key=''.join([chr(i) for i in [((ord(c)-dis) if ord(c)>=97+dis else 26+ord(c)-dis) for c in ss]])
            if key in allGroups:
                allGroups[key].append(ss)
            else:
                allGroups[key]=[ss]
        return [sorted(l) for l in allGroups.values()]




    # too slow, n**2
    def groupStringsOld(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        strings=sorted(strings)
        results=[]

        for i in xrange(len(strings)):
            if strings[i]:
                results.append([strings[i]])
                for j in xrange(i+1,len(strings)):
                    if not strings[j]:
                        continue

                    if len(strings[j])==len(strings[i]):
                        diff=ord(strings[j][0])-ord(strings[i][0])
                        match=True
                        for a,b in zip(strings[j][1:], strings[i][1:]):
                            if ord(a)-ord(b)!=diff and (ord(a)-ord(b)-diff) not in [26,-26]:
                                match=False
                                break
                        if match:
                            results[-1].append(strings[j])
                            strings[j]=0
        return results

if __name__ == '__main__':
    s=Solution()
    print s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
    print s.groupStringsOld(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])

    print s.groupStrings(['a','b','b'])
    print s.groupStringsOld(['a','b','b'])




