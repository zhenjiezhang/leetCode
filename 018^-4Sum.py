'''
18. 4Sum
Total Accepted: 58690 Total Submissions: 258221 Difficulty: Medium

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

    Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
    The solution set must not contain duplicate quadruplets.

    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)

'''
'''
http://bangbingsyb.blogspot.hk/2014/11/leetcode-4sum.html

既然已经做了2sum, 3sum, 3sum closest。自然能推广到4sum。但这里希望能推广到更普遍的k-sum问题。这里使用递归的思路：

1. k-sum问题可以转化为(k-1)-sum问题：对于数组中每个数A[i]，在A[i+1:n-1]中寻找target-A[i]的(k-1)-sum问题。
2. 直到k=2时，用2sum的双指针扫描来完成。

去重复解的技巧和3Sum问题一模一样。
    

class Solution {
public:
    vector<vector<int> > fourSum(vector<int> &num, int target) {
        vector<vector<int>> allSol;
        vector<int> sol;
        sort(num.begin(),num.end());
        kSum(num, 0, num.size()-1, target, 4, sol, allSol);
        return allSol;
    }
    
    void kSum(vector<int> &num, int start, int end, int target, int k, vector<int> &sol, vector<vector<int>> &allSol) {
        if(k<=0) return;
        if(k==1) {
            for(int i=start; i<=end; i++) {
                if(num[i]==target) {
                    sol.push_back(target);
                    allSol.push_back(sol);
                    sol.pop_back();
                    return;
                }
            }
        } 
        
        if(k==2) {
            twoSum(num, start, end, target, sol, allSol);
            return;
        }
    
        for(int i=start; i<=end-k+1; i++) {
            if(i>start && num[i]==num[i-1]) continue;
            sol.push_back(num[i]);
            kSum(num, i+1, end, target-num[i], k-1, sol, allSol);
            sol.pop_back();
        }
    }
    
    void twoSum(vector<int> &num, int start, int end, int target, vector<int> &sol, vector<vector<int>> &allSol) {
        while(start<end) {
            int sum = num[start]+num[end];
            if(sum==target) {
                sol.push_back(num[start]);
                sol.push_back(num[end]);
                allSol.push_back(sol);
                sol.pop_back();
                sol.pop_back();
                start++;
                end--;
                while(num[start]==num[start-1]) start++;
                while(num[end]==num[end+1]) end--;
            }
            else if(sum<target)
                start++;
            else
                end--;
        }
    }
};

'''


class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):

        newNum=[]
        filter=dict()
        for i in num:
            if i in filter:
                if (filter[i]==3 and i*4!=target) or filter[i]==4:
                    continue
                else:
                    newNum.append(i)
                    filter[i]+=1
            else:
                newNum.append(i)
                filter[i]=1

        num=sorted(newNum)

        pairs=[[x,y] for x in xrange(len(num)-1) for y in xrange(x+1,len(num))]
        results=set()

        twoSums=dict()
        for pair in pairs:
            if num[pair[0]]+num[pair[1]] in twoSums:
                twoSums[num[pair[0]]+num[pair[1]]].append(pair)
            else:
                twoSums[num[pair[0]]+num[pair[1]]]=[pair]

        for num1 in twoSums:
            num2=target-num1
            if num2 >= num1 and num2 in twoSums:
                combinations=[pair1+pair2 for pair1 in twoSums[num1] for pair2 in twoSums[num2] if pair2[0]>pair1[1]]
                for comb in combinations:
                    results.add(tuple([num[i] for i in comb]))
        
        
        return [list(sums) for sums in results]


if __name__=="__main__":
    solution=Solution()
    print solution.fourSum([1,0,-1,0,-2,2,1,1,1,1],0)
    # print solution.fourSum([1,0,-1,0,-2,2], 0)
    print solution.fourSum([2,1,0,-1], 2)

         







