class Solution(object):
    # this is bfs, dfs could actually be faster.
    
    def coinChange(self, coins, amount):
        level = seen = {0}
        number = 0
        while level:
            if amount in level:
                return number
            newLevel=set()
            

            level = {a+c for a in level for c in coins if a+c <= amount and a+c not in seen}
            seen |= level
            number += 1
        return -1


if __name__ == '__main__':
    solution=Solution()
    for n in xrange(1):
        print n, solution.coinChange([186,419,83,408],6249)
