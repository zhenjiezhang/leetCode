'''
68. Text Justification
Total Accepted: 28696 Total Submissions: 184905 Difficulty: Hard

Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Note: Each word is guaranteed not to exceed L in length.

click to show corner cases.
Corner Cases:

    A line other than the last line might contain only one word. What should you do in this case?
    In this case, that line should be left-justified.
'''

    # Same strategy, very concise:

# vector<string> fullJustify(vector<string> &words, int L) {
#     vector<string> res;
#     for(int i = 0, k, l; i < words.size(); i += k) {
#         for(k = l = 0; i + k < words.size() and l + words[i+k].size() <= L - k; k++) {
#             l += words[i+k].size();
#         }
#         string tmp = words[i];
#         for(int j = 0; j < k - 1; j++) {
#             if(i + k >= words.size()) tmp += " ";
#             else tmp += string((L - l) / (k - 1) + (j < (L - l) % (k - 1)), ' ');
#             tmp += words[i+j+1];
#         }
#         tmp += string(L - tmp.size(), ' ');
#         res.push_back(tmp);
#     }
#     return res;
# }

class Solution:
	def fullJustify(self, strings, L):
		i=0
		result=[]
		while i<len(strings):
			line=[strings[i]]
			lineCount=len(strings[i])
			i+=1
			while i<len(strings) and lineCount+len(strings[i])<L:
				line.append(strings[i])
				lineCount+=len(strings[i])+1
				i+=1

			result.append(self.assemble(line, L) if i<len(strings) else self.assemble(line, L, last=True))
		return result

# making extra list of paddings and zipping together spent more time than simple for loops.  but zipping is neat
	def assemble(self, line, L, last=False):
		if len(line)==1:
			return line[0]+' '*(L-len(line[0]))
		if last:
			paddingList=[' ' for _ in xrange(len(line)-1)]
			res=''.join([s1+s2 for s1, s2 in zip(line, paddingList)]+[line[-1]])
			return res+' '*(L-len(res))


		paddingNum=L-sum([len(s) for s in line])
		spaceNum=len(line)-1
		paddingRight=paddingNum/spaceNum
		paddingLeft=paddingRight+1
		firstRight=paddingNum%spaceNum

		paddingList=[' '*paddingLeft for _ in xrange(firstRight)]+[' '*paddingRight for _ in xrange(spaceNum-firstRight)]
		return ''.join([s1+s2 for s1, s2 in zip(line, paddingList)]+[line[-1]])




			



	def fullJustifyOld(self, strings, L):

		lines=[]
		currentCount=0
		i=0
		start=0
		end=0

		if len(strings)==0 or L==0:
			return [""]

		while (i<len(strings)):
			wordLen=len(strings[i])
			if currentCount+wordLen <= L:
				i+=1
				currentCount+=wordLen+1
				continue
			else:
				end=i-1
				
				slots=end-start
				spaces=L-currentCount+1

				if slots==0:
					lines.append(strings[start]+" "*(L-len(strings[start])))
					currentCount=wordLen+1
					start=i
					i+=1
					

				else:
					extra=spaces % slots
					line=""

					for j in range(extra):
						line+=strings[start+j]+" "*(spaces/slots+2)
					for j in range(slots-extra):
						line+=strings[start+extra+j]+" "*(spaces/slots+1)
					line+=strings[end]
					lines.append(line)
					currentCount=wordLen+1

					start=i

					i+=1

		lastline=""
		end=len(strings)-1
		if end==start:
			lines.append(strings[start]+" "*(L-len(strings[start])))
			return lines
		for i in range(start,end+1):
			lastline+=strings[i]+" "
		lastline+=" "*(L-len(lastline))
		lines.append(lastline)

		return lines


if __name__=="__main__":
	solution=Solution()

	for s in solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16):
		print s
	print 
	for s in solution.fullJustify(["a","b","c","d","e"], 1):
		print s
	print 

	for s in solution.fullJustify(["What","must","be","shall","be."], 12):
		print s
	print 

	for s in solution.fullJustify(["Listen","to","many,","speak","to","a","few."], 6):
		print s











