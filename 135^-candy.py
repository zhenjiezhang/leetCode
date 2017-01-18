'''
135. Candy
Total Accepted: 46807 Total Submissions: 215444 Difficulty: Hard

There are N children standing in a line. Each child is assigned a ratings value.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher ratings get more candies than their neighbors.

What is the minimum candies you must give? 
'''



# way too complicated.  

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if not ratings:
            return 0
        candies=[1]*len(ratings)
        for p in xrange(len(ratings)-1):
            if ratings[p]<ratings[p+1]:
                candies[p+1]=candies[p]+1
        for p in xrange(len(ratings)-1, 0, -1):
            if ratings[p]<ratings[p-1]:
                candies[p-1]=max(candies[p]+1, candies[p-1])
        return sum(candies)


    def candyOnePath(self, ratings):
        if not ratings:
            return 0

        p1=p2=0
        candies=[1]*len(ratings)
        while p1<len(ratings):
            while p1<(len(ratings)-1) and ratings[p1]==ratings[p1+1]:
                p1+=1

            if p1==len(ratings)-1:
                return sum(candies)

            if ratings[p1]<ratings[p1+1]:
                while p1<(len(ratings)-1) and ratings[p1]<ratings[p1+1]:
                    p1+=1
                    candies[p1]=candies[p1-1]+1

            elif ratings[p1]>ratings[p1+1]:
                depth=0
                while p1<(len(ratings)-1) and ratings[p1]>ratings[p1+1]:
                    p1+=1
                    depth+=1

                for p in xrange(p1-1, p1-depth, -1):
                    candies[p]=candies[p+1]+1
                candies[p1-depth]=max(candies[p1-depth], candies[p1-depth+1]+1)







    def candyOld(self, ratings):
        troughs=[]
        candies=[1 for i in range(len(ratings))]

        if len(ratings)<2:
        	return sum(range(len(ratings)+1))

        i=0
        if ratings[i]<ratings[i+1]:
            troughs.append(i)
        elif ratings[i]==ratings[i+1]:
            i+=1
            while (i+1)<len(ratings) and ratings[i]==ratings[i+1]:
                i=i+1
            if i+1>=len(ratings) or ratings[i]<ratings[i+1]:
                troughs.append(i)

        while i<(len(ratings)-1):
            if ratings[i]<ratings[i-1] and ratings[i]<ratings[i+1]:
                troughs.append(i)
            elif ratings[i]<ratings[i-1] and ratings[i]==ratings[i+1]:
                i+=1
                while (i+1)<len(ratings) and ratings[i]==ratings[i+1]:
                    i=i+1
                if i+1>=len(ratings) or ratings[i]<ratings[i+1]:
                    troughs.append(i)
            i+=1

        if ratings[len(ratings)-1] < ratings[len(ratings)-2]:
        	troughs.append(len(ratings)-1)

        for i in troughs:
        	j=i
        	candyNum=1
        	while j-1>=0 and ratings[j-1]>=ratings[j]:
        		# if candies[j-1]>=candyNum+1:
        		# 	break

        		candies[j-1]=max(candyNum+1,candies[j-1]) if ratings[j-1]>ratings[j] else max(1,candies[j-1])
        		candyNum=candies[j-1]
        		j-=1

        	j=i
        	candyNum=1
        	while j+1<len(ratings) and ratings[j+1]>=ratings[j]:
        		candies[j+1]=candyNum+1 if ratings[j+1]>ratings[j] else 1
        		candyNum=candies[j+1]
        		j+=1



        # print ratings
        # print candies

        return sum(candies)

                        




if __name__=="__main__":
    solution=Solution()
    print solution.candy([1,1,5 ,2,2,2,3,3,4,1,4,0,0])
    print solution.candy([2,1])
    print solution.candy([4,2,3,4,1])
    print solution.candyOld([1,1,5 ,2,2,2,3,3,4,1,4,0,0])
    print solution.candyOld([2,1])
    print solution.candyOld([4,2,3,4,1])


