'''
187. Repeated DNA Sequences
Total Accepted: 35624 Total Submissions: 151059 Difficulty: Medium

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].



A very nice bit encoding:

public class Solution {
    public List<String> findRepeatedDnaSequences(String DNA) {
        ArrayList<String> res = new ArrayList<String>();
        if(DNA.length()<10)    return res;
        HashSet<Integer> once = new HashSet<Integer>();
        HashSet<Integer> twice = new HashSet<Integer>();
        int[] map = new int[26];
        map['A'-'A'] = 0;
        map['C'-'A'] = 1;
        map['G'-'A'] = 2;
        map['T'-'A'] = 3;
        int enc = 0;
        for(int i=0; i<9; ++i){
            enc <<=2;
            enc |= map[DNA.charAt(i)-'A'];
        }
        for(int j=9; j<DNA.length(); ++j){
            enc <<=2;
            enc &= 0xfffff;
            enc |= map[DNA.charAt(j)-'A'];
            if(!once.add(enc) && twice.add(enc))
                res.add(DNA.substring(j-9,j+1));
        }
        return res;
    }
}

'''
class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        stock=set()
        results=set()
        if len(s)<10:
            return list(results)
        start=0
        while start+9<len(s):
            if s[start:start+10] in stock:
                if s[start:start+10] not in results:
                    results.add(s[start:start+10])
            else:
                stock.add(s[start:start+10])
            start+=1
        return list(results)

