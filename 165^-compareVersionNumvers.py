'''
165. Compare Version Numbers
Total Accepted: 43333 Total Submissions: 260113 Difficulty: Easy

Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''
class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        if version1==version2:
            return 0

        v1=(version1).split('.')
        v2=(version2).split('.')
        # it is important to add 0 tails, as 1.0==1 is true
        v1=[int(i) for i in v1]+[0]*(len(v2)-len(v1))
        v2=[int(i) for i in v2]+[0]*(len(v1)-len(v2))

        return 1 if v1>v2 else (0 if v1==v2 else -1)


print Solution().compareVersion('1','1.0.0.1')
