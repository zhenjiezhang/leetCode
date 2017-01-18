'''
47. Permutations II
Total Accepted: 58105 Total Submissions: 215981 Difficulty: Medium

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1]. 
'''

# I use hash set, but is there a better solution?

class Solution:

	def permuteUnique(self, num):
		self.num=sorted(num)
		self.result=[]
		self.swapAll()
		return self.result

	def swapAll(self, pos=0):
		print pos, self.num
		if self.num[pos]==self.num[-1]:
			self.result.append(list(self.num))
			return

		i=pos
		while i<len(self.num):
			print i

			self.num[pos], self.num[i]=self.num[i], self.num[pos]
			self.swapAll(pos+1)
			self.num[pos], self.num[i]=self.num[i], self.num[pos]

			i+=1
			if i< len(self.num) and self.num[i]==self.num[i-1]:
				i+=1


			






	def permuteUniqueOld(self, num):
		l=len(num)
		output=[]
		if l==1:
			output.append(num)
			return output
		else:
			last=num[-1]
			tmp=self.permuteUnique(num[0:-1])

			outputSet=set()

			for seq in tmp:
				outputSet.add(tuple(seq+[last]))
				for i in range(len(seq)):
					outputSet.add(tuple(seq[0:i]+[last]+seq[i:len(seq)]))

			for seq in outputSet:
				output.append(list(seq))

		return output



if __name__=="__main__":
	solution=Solution()
	print solution.permuteUnique([3,3,0,3])


