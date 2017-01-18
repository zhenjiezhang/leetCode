'''
65. Valid Number
Total Accepted: 39447 Total Submissions: 332804 Difficulty: Hard

Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition. 
'''


#short but not the intention of the examinor.  Should write a manual check.
# this is boring and stupid

class Solution:
# @param s, a string
# @return a boolean

    def isNumber(self, s):
        s=s.strip()
        if s and s[0] in {'+','-'}:
            s=s[1:]

        # split with e, should have at most 2 parts, and each parts should not be empty
        eSep=s.split('e')
        if len(eSep)>2:
            return False
        if len(eSep)==2:
            if eSep[1] and eSep[1][0] in {'+','-'}:
                eSep[1]=eSep[1][1:]
        for s in eSep:
            if not s:
                return False

        # split each side of e with .
        # each side of e-split should not have more than 2 parts splitted by .
        # for a . split, at least one side should have content
        # the second part of e-split should not have a .
        eSep=[s.split('.') for s in eSep]
        for s in eSep:
            if len(s)>2:
                return False
            if len(s)==2:
                if not s[0] and not s[1]:
                    return False
        if len(eSep)==2:
            if eSep[1] and len(eSep[1])>1:
                return False



        # flatten all the splits, and check if they are digits.  
        # ''s are ignored at this point. but there should  be at least one part not empty
        eSep=[ss for s in eSep for ss in s]

        thereIsNum=False
        for s in eSep:
            if s and not s.isdigit():
                return False
            elif s:
                thereIsNum=True

        return thereIsNum




'''
old
'''

    def isNumberOld(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

if __name__ == '__main__':
    s=Solution()
    # print s.isNumber('6e6.5')
    # print s.isNumber('66.5')

    print s.isNumber('005047e+6')

