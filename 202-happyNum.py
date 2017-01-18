'''
202. Happy Number
Total Accepted: 52086 Total Submissions: 147458 Difficulty: Easy

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1




A interesting observation:

class Solution { public: int loop[8] = {4,16,37,58,89,145,42,20};

bool inLoop(int n){
    for(auto x: loop){
        if(x == n) return true;
    }
    return false;
}

bool isHappy(int n) {
    if(n == 1) return true;
    if(inLoop(n)) return false;
    int next = 0;
    while(n){
        next += (n%10)*(n%10);
        n /= 10;
    }
    return isHappy(next);
}

};

proof:

1.loop number is less than 162.

Assume f(x) is the sum of the squares of x's digits. let's say 0 < x <= 9,999,999,999 which is larger than the range of an int. f(x) <= 9^2 * 10 = 810. So no mater how big x is, after one step of f(x), it will be less than 810.The most large f(x) value (x < 810) is f(799) = 211. And do this several times: f(211) < f(199) = 163. f(163) < f(99) = 162. So no mater which x you choose after several times of f(x),it finally fall in the range of [1,162] and can never get out.

2.I check every unhappy number in range of [1,162] , they all fall in loop {4,16,37,58,89,145,42,20} ,which means every unhappy number fall in this loop.


    '''

class Solution(object):

    def sumOfDig(self, n):
        s=0
        while n>0:
            s+=(n%10)**2
            n/=10
        return s

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        history=set([n])
        while n!=1:
            n=self.sumOfDig(n)
            
            if n in history:
                return False
            history.add(n)

        return True

if __name__ == '__main__':
    print Solution().isHappy(18)




        