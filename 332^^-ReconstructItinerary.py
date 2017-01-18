'''
332. Reconstruct Itinerary
Total Accepted: 3202 Total Submissions: 13878 Difficulty: Medium

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

    If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
    All airports are represented by three capital letters (IATA code).
    You may assume all tickets form at least one valid itinerary.

Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].

Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order. 
'''

class Solution(object):


    def findItinerary(self, tickets):
        from collections import defaultdict
        startCityMap=defaultdict(list)
        tickets.sort(reverse=True)
        for s,t in tickets:
            startCityMap[s].append(t)

        res=[]

        #very clever method!

        
        def dfs(startCity):
            while startCityMap[startCity]:
                dfs(startCityMap[startCity].pop())
            res.append(startCity)
        dfs('JFK')
        return res[::-1]

        






    def findItineraryOld(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        startCityMap=dict()
        self.totalVisit=len(tickets)

        tickets.sort(reverse=True)
        for f,t in tickets:
            startCityMap.setdefault(f,[]).append(t)
        

        def dfs(startCity):
            if self.totalVisit==0:
                return [startCity]
            if startCity not in startCityMap or not startCityMap[startCity]:
                return []

            destinations=startCityMap[startCity]
            self.totalVisit-=1

            for i in xrange(len(destinations)-1, -1, -1):
                tmp=destinations.pop(i)
                path=dfs(tmp)
                if not path:
                    destinations.insert(i,tmp)
                else:
                    return [startCity]+path
            self.totalVisit+=1
            return []
        return dfs('JFK')

if __name__=="__main__":
    s=Solution()
    print s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])
    # print s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])


    
