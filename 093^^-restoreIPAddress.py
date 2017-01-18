'''
93. Restore IP Addresses
Total Accepted: 48535 Total Submissions: 216479 Difficulty: Medium

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter) 
'''
'''
other ways:
public class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> res = new ArrayList<String>();
        int len = s.length();
        for(int i = 1; i<4 && i<len-2; i++){
            for(int j = i+1; j<i+4 && j<len-1; j++){
                for(int k = j+1; k<j+4 && k<len; k++){
                    String s1 = s.substring(0,i), s2 = s.substring(i,j), s3 = s.substring(j,k), s4 = s.substring(k,len);
                    if(isValid(s1) && isValid(s2) && isValid(s3) && isValid(s4)){
                        res.add(s1+"."+s2+"."+s3+"."+s4);
                    }
                }
            }
        }
        return res;
    }
    public boolean isValid(String s){
        if(s.length()>3 || s.length()==0 || (s.charAt(0)=='0' && s.length()>1) || Integer.parseInt(s)>255)
            return false;
        return true;
    }
}




public List<String> restoreIpAddresses(String s) {
    List<String> solutions = new ArrayList<String>();
    restoreIp(s, solutions, 0, "", 0);
    return solutions;
}

private void restoreIp(String ip, List<String> solutions, int idx, String restored, int count) {
    if (count > 4) return;
    if (count == 4 && idx == ip.length()) solutions.add(restored);

    for (int i=1; i<4; i++) {
        if (idx+i > ip.length()) break;
        String s = ip.substring(idx,idx+i);
        if ((s.startsWith("0") && s.length()>1) || (i==3 && Integer.parseInt(s) >= 256)) continue;
        restoreIp(ip, solutions, idx+i, restored+s+(count==3?"" : "."), count+1);
    }
}
'''

class Solution:

    def restoreIpAddresses(self, s):
        IPs=[
        [[],[],[]]
        ]

        for i in xrange(len(s)-1):
            ipSegsEndingHere=[[],[],[]]

            oneSeg=int(s[:i+1])
            ipSegsEndingHere[0]=[s[:i+1]] if i<=2 and 0<=oneSeg<=255 and str(oneSeg)==s[:i+1] else []

            ipSegsEndingHere[1]=[seg+'.'+s[i] for seg in IPs[-1][0]]\
            +([seg+'.'+s[i-1:i+1] for seg in IPs[-2][0]] if i>=2 and s[i-1]!='0' else [])\
            +([seg+'.'+s[i-2:i+1] for seg in IPs[-3][0]] if i>=3 and s[i-2]!='0' and 0<=int(s[i-2: i+1])<=255 else [])


            ipSegsEndingHere[2]=[seg+'.'+s[i] for seg in IPs[-1][1]]\
            +([seg+'.'+s[i-1:i+1] for seg in IPs[-2][1]] if i>=3 and s[i-1]!='0' else [])\
            +([seg+'.'+s[i-2:i+1] for seg in IPs[-3][1]] if i>=4 and s[i-2]!='0' and 0<=int(s[i-2: i+1])<=255 else [])

            IPs.append(ipSegsEndingHere)

        return([seg+'.'+s[-1] for seg in IPs[-1][2]]\
            +([seg+'.'+s[-2:] for seg in IPs[-2][2]] if len(s)>=5 and s[-2]!='0' else [])\
            +([seg+'.'+s[-3:] for seg in IPs[-3][2]] if len(s)>=6 and s[-3]!='0' and 0<=int(s[-3:])<=255 else [])\
            )
        

'''
old
'''

    # @param s, a string
    # @return a list of strings
    def isLastSeg(self,s):
        n=int(s)
        if n>=0 and n<=255:
            return True
    def isLast2Seg(self,s):
        segments=[]
        
        for i in xrange(1,min(4,len(s))):
            n=int(s[:i])
            if n>=0 and n<=255 and self.isLastSeg(s[i:]):
                if str(int(s[:i]))==s[:i] and str(int(s[i:]))==s[i:]:
                    segments+=[s[:i]+'.'+s[i:]]
        return segments

    def isLast3Seg(self,s):
        segments=[]

        for i in xrange(1,min(4,len(s)-1)):
            n=int(s[:i])
            subsegs=self.isLast2Seg(s[i:])
            if n>=0 and n<=255 and subsegs:
                if str(int(s[:i]))==s[:i]:
                    segments+=[s[:i]+'.'+subseg for subseg in subsegs]
        return segments

    def restoreIpAddressesOld(self, s):
        
        IPs=[]
        for i in xrange(1,min(4,len(s)-2)):
            n=int(s[:i])
            subsegs=self.isLast3Seg(s[i:])
            if n>=0 and n<=255 and subsegs:
                if str(int(s[:i]))==s[:i]:
                    IPs+=[s[:i]+'.'+subseg for subseg in subsegs]
        return IPs


if __name__ == '__main__':
    solution=Solution()
    print solution.restoreIpAddresses("17165657")
    print solution.restoreIpAddressesOld("17165657")

    # print solution.restoreIpAddresses("010010")

