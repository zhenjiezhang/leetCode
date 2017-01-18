class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    


    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # this does not work. the old one works, think about why
    
    def threeSum(self, nums):
        result=[]
        dup=dict()
        negative=[]
        positive=[]
        for n in nums:
            if n==0 and 0 in dup and dup[0] and len(results)==0:
                results.append([0,0,0])

            if n not in dup:
                (negative if n<=0 else positive).append(n)
                dup[n]=0

            elif n in dup and not dup[n]:
                (negative if n<0 else positive).append(n)
                dup[n]=1

        negative=sorted(negative)
        positive=sorted(positive)


        allNums=set(nums)

        for i in xrange(len(negative)):
            for j in xrange(i+1, len(negative)):
                if -negative[i]-negative[j] in allNums:
                    result.append([negative[i], negative[j], -negative[i]-negative[j]])

        for i in xrange(len(positive)):
            for j in xrange(i+1, len(positive)):
                if -positive[i]-positive[j] in allNums:
                    result.append([positive[i], positive[j], -positive[i]-positive[j]])

        return result






    def threeSum_old(self, num):
    	results=[]

        hashsets=[set(),set()] # hashsets[0] for negative numbers, hashsets[0] for 0 and positive numbers
        duplicates=set()	#record duplicate numbers, triplets and above should be counted as duplets, except in case of triplet 0's.
        for n in num:
        	if n==0 and 0 in hashsets[1] and 0 in duplicates and len(results)==0:
        		results.append([0,0,0])
        	if n <0:
        		if n in hashsets[0]:
        			duplicates.add(n)
        		else:
	        		hashsets[0].add(n)
        	else:
        		if n in hashsets[1]:
        			duplicates.add(n)
        		else:
	        		hashsets[1].add(n)
        sortedLists=[sorted(hashsets[0]),sorted(hashsets[1])]

        for x in xrange(len(sortedLists[0])):
        	if sortedLists[0][x] in duplicates:
        		if -2*sortedLists[0][x] in hashsets[1]:
        			results.append([sortedLists[0][x],sortedLists[0][x],-2*sortedLists[0][x]])
        	for y in xrange(x+1,len(sortedLists[0])):
        		if -(sortedLists[0][x]+sortedLists[0][y]) in hashsets[1]:
        			results.append([sortedLists[0][x],sortedLists[0][y],-sortedLists[0][x]-sortedLists[0][y]])

        for x in xrange(len(sortedLists[1])):
        	if sortedLists[1][x] in duplicates:
        		if -2*sortedLists[1][x] in hashsets[0]:
        			results.append([-2*sortedLists[1][x],sortedLists[1][x],sortedLists[1][x]])
        	for y in xrange(x+1,len(sortedLists[1])):
        		if -(sortedLists[1][x]+sortedLists[1][y]) in hashsets[0]:
        			results.append([-sortedLists[1][x]-sortedLists[1][y],sortedLists[1][x],sortedLists[1][y]])

     	
     	return results

if __name__=="__main__":
	solution=Solution()
	print solution.threeSum_old([-1,0,1,2,-1,-4])
	# print solution.threeSum([9,-4,-5,8,-5,7,5,-6,-4,-13,9,-10,-13,-6,2,-15,-13,-9,-4,-13,-9,-9,13,-13,-9,9,-15,1,0,-14,-8,-13,-11,-5,2,0,9,14,9,-9,8,-5,-12,10,-3,5,3,-1,12,14,1,10,12,-1,13,-12,-14,13,4,-7,6,4,-5,11,6,4,-12,0,3,4,-2,-3,7,1,14,-11,-8,2,-5,11,-7,3,6,-9,9,4,-14,10,-6,-2,-11,-14,-13,-9,4,0,11,-1,-15,-9,-12,-1,3,10,7,-5,6,6,12,8,2,-9,-4,-6,-11,-9,5,-10,-14,-15,3])
