'''
76. Minimum Window Substring
Total Accepted: 50521 Total Submissions: 249800 Difficulty: Hard

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"

Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S. 
'''


# this is quite fast (> 93%),  but a bit long
'''


There is a short one!

string minWindow(string s, string t) {
        vector<int> map(128,0);
        for(auto c: t) map[c]++;
        int counter=t.size(), begin=0, end=0, d=INT_MAX, head=0;
        while(end<s.size()){
            if(map[s[end++]]-->0) counter--; //in t
            while(counter==0){ //valid
                if(end-begin<d)  d=end-(head=begin);
                if(map[s[begin++]]++==0) counter++;  //make it invalid
            }  
        }
        return d==INT_MAX? "":s.substr(head, d);
    }
'''
from collections import deque, Counter
class Solution:
    # @return a string


    def minWindow(self, S, T):
        # first get a count of all characters in T
        tCounter=Counter(T)
        # position dict to record the positions of T-characters in current window.  
        # A deque is used, with maxlen set to count in T for each character
        positions={t:deque(maxlen=tCounter[t]) for t in tCounter}

        # find the first window in S that contains the whole collection of characters in T
        i=0
        counter=0
        while i <  len(S) and counter<len(T):
            if S[i] in tCounter:
                if len(positions[S[i]])<tCounter[S[i]]:
                    counter+=1
                positions[S[i]].append(i)
            i+=1

        # if no such window is found, return empty
        if counter<len(T):
            return ''

        end=i
        # now find the start of this window, by using a second pointer 'start'
        start=0
        while start<len(S):
            if S[start] in tCounter and positions[S[start]][0]==start:
                break
            start+=1

        minLen=end-start
        minStart=start
        minEnd=end

        # iterate through S, update positions when needed.  
        # When the start character is encoutered, find the new start using the second pointer, and update minLen, minStart, minEnd when needed
        for i in xrange(end, len(S)):
            if S[i] in tCounter:
                positions[S[i]].append(i)
                if S[i]==S[start]:
                    end=i+1
                    start+=1
                    while S[start] not in positions or positions[S[start]][0]!=start:
                        start+=1
                    if end-start<minLen:
                        minLen=end-start
                        minStart=start
                        minEnd=end
        return S[minStart: minEnd]









    def minWindowOld(self, S, T):
      TCount=dict()
      currentWindow=dict()

      for i in T:
        currentWindow[i]=0
        if i in TCount:
          TCount[i]+=1
        else:
          TCount[i]=1


      currentCount=0

      window=len(S)+1
      thisStart=thisEnd=start=0
      end=-1

      for i in range(len(S)):
        if S[i] in TCount:
          thisStart=thisEnd=i
          break

      

      for i in range(thisStart, len(S)):


        if S[i] in TCount:
          currentWindow[S[i]]+=1
          if currentWindow[S[i]] <=TCount[S[i]]:
            currentCount+=1
            if currentCount==len(T):
              while (S[thisStart] not in currentWindow) or (currentWindow[S[thisStart]]>TCount[S[thisStart]]):
                
                if (S[thisStart] in currentWindow):
                  currentWindow[S[thisStart]]-=1

                thisStart+=1




              thisEnd=i
              if thisEnd-thisStart+1<window:
                start=thisStart
                end=thisEnd
                window=end-start+1

              currentWindow[S[thisStart]]-=1
              thisStart+=1              
              currentCount-=1
              # print thisStart, currentCount


      return S[start:end+1]

if __name__=="__main__":
    solution=Solution()
    # print solution.minWindow("12trjlkfsdfdsfsgfsfds4ewrewr","trffr")
    # print solution.minWindowOld("12trjlkfsdfdsfsgfsfds4ewrewr","trffr")

    # print solution.minWindow("bba", "ab")
    # print solution.minWindow("","")
    print solution.minWindow("bdab", "ab")




          