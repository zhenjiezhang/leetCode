'''
170. Two Sum III - Data structure design
Total Accepted: 8165 Total Submissions: 33698 Difficulty: Easy

Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,

add(1); add(3); add(5);
find(4) -> true
find(7) -> false

'''

class TwoSum:

    # initialize your data structure here
    def __init__(self):
        self.nums={}        

    # @return nothing
    def add(self, number):
        if number in self.nums:
            self.nums[number]+=1
        else:
            self.nums[number]=1
        

    # @param value, an integer
    # @return a Boolean
    def find(self, value):
        for number in self.nums:
            target=value-number
            if target in self.nums and  (target!=number or self.nums[target]>1):
                	return True

        return False

if __name__ == '__main__':
	solution=TwoSum()
	solution.add(2)
	solution.add(5)
	print solution.find(7)

        