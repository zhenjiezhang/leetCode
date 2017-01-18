'''
321. Create Maximum Number
Total Accepted: 1373 Total Submissions: 7364 Difficulty: Hard

Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.

Example 1:

nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:

nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:

nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9] 
'''



''''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def maxNumber(self, nums1, nums2, k):

    def prep(nums, k):
        drop = len(nums) - k
        out = []
        for num in nums:
            while drop and out and out[-1] < num:
                out.pop()
                drop -= 1
            out.append(num)
        return out[:k]

    def merge(a, b):
        return [max(a, b).pop(0) for _ in a+b]

    return max(merge(prep(nums1, i), prep(nums2, k-i))
               for i in range(k+1)
               if i <= len(nums1) and k-i <= len(nums2))


'''
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        # result=[0]*k

        # for length1 in xrange(k+1):
        #     ans=[]
        #     if len(nums1)>=length1 and len(nums2)>=k-length1:
        #         ans1=self.maxNumber_single(nums1, length1)
        #         ans2=self.maxNumber_single(nums2, k-length1)

        #         i=0
        #         p1=p2=0
        #         while i<k:
        #             if ans1[p1:]>ans2[p2:]:
        #                 ans.append(ans1[p1])
        #                 p1+=1
        #             else:
        #                 ans.append(ans2[p2])
        #                 p2+=1

        #             i+=1

        #         if ans>result:
        #             result=ans
        # return result
        def merge(a, b):
            return [max(a, b).pop(0) for _ in a+b]
        return max(merge(self.maxNumber_single(nums1, i), self.maxNumber_single(nums2, k-i))
               for i in range(k+1)
               if i <= len(nums1) and k-i <= len(nums2))


    '''
    this is so much faster than my method although the same worst case complexity!
    '''
    def maxNumber_single(self, nums, k):
        drop = len(nums) - k
        out = []
        for num in nums:
            while drop and out and out[-1] < num:
                out.pop()
                drop -= 1
            out.append(num)
        return out[:k]

        # res=[]
        # if k==0:
        #     return res

        # stack=[]
        # for i in xrange(len(nums)-k):
        #     while stack and stack[-1]<nums[i]:
        #         stack.pop()
        #     stack.append(nums[i])

        # for i in xrange(k):
            
        #     while stack and stack[-1]<nums[len(nums)-k+i]:
        #         stack.pop()
        #     stack.append(nums[len(nums)-k+i])
        #     res.append(stack[i])
        #     stack[i]=float('inf')

        # return res



    def maxNumber_singleOld(self, nums, k):
        ans=[]
        start=0
        for i in xrange(k):
            maxElem=-float('inf')
            for j in xrange(start, len(nums)-k+i+1):
                if nums[j]>maxElem:
                    maxElem=nums[j]
                    start=j+1

            ans.append(maxElem)
        return ans

if __name__ == '__main__':
    s=Solution()
    print s.maxNumber([3,9],[8,9],3)
    print s.maxNumber([6,7],[6,0,4],5)



