class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        l=len(gas)
        netGasGain=[gas[i]-cost[i] for i in xrange(len(gas))]
        netGasGain.extend(netGasGain)

        start=0
        while start<l:
            gasRemaining=0
            station=start
            while station<start+l and gasRemaining>=0:
                gasRemaining+=netGasGain[station]
                station+=1
            if station==start+l and gasRemaining>=0:
                return start
            else:
                start=station
        return -1






    def canCompleteCircuitOld(self, gas, cost):
        netGasGain=[gas[i]-cost[i] for i in xrange(len(gas))]
        start=0
        while start <len(gas):
            while start<len(gas) and netGasGain[start]<0:
                start+=1
            if start==len(gas):
                return -1
            gasRemaining=netGasGain[start]
            station=start+1 if start<len(gas)-1 else 0
            legs=1
            while gasRemaining+netGasGain[station]>=0:
                if station==start:
                    return start
                gasRemaining+=netGasGain[station]
                station=(station+1) if station < len(gas)-1 else 0
                legs+=1
            start+=legs+1
        return -1

if __name__ == '__main__':
    solution=Solution()
    gas=[3,5,2,1]
    cost=[2,6,4,1]
    print solution.canCompleteCircuit(gas,cost)
    print solution.canCompleteCircuitOld(gas,cost)




