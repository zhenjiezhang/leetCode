class Solution(object):
    def containsNearbyAlmostDuplicate_toyMemoryError(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        hashSet=set()
        for i in nums[:k]:
            hashSet=hashSet | set(range(i-t,i+1))

        if len(nums) <=k:
            return len(hashSet)<len(nums)*(t+1)

        if len(hashSet) < k*(t+1):
            return True

        for i in xrange(k,len(nums)):
            # print hashSet
            hashSet=hashSet | set(range(nums[i]-t,nums[i]+1))
            # print hashSet, (k+1)*t

            if len(hashSet) < (k+1)*(t+1):
                return True

            hashSet=hashSet-set(range(nums[i-k]-t,nums[i-k]+1))
        return False

    def containsNearbyAlmostDuplicate(self,nums,k,t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t<0:
            return False

        elif t==0:
            numsScaled=nums
        else:
            numsScaled=[n/t for n in nums]

        hashMap={}

        for i in xrange(len(nums)):
            if numsScaled[i] in hashMap:
                return True

            if numsScaled[i]-1 in hashMap:
                if nums[i]-hashMap[numsScaled[i]-1]<=t:
                    return True

            if numsScaled[i]+1 in hashMap:
                if hashMap[numsScaled[i]+1]-nums[i]<=t:
                    return True

            hashMap[numsScaled[i]]=nums[i]

            if i>=k:
                hashMap.pop(numsScaled[i-k])

        return False

if __name__ == '__main__':
    print Solution().containsNearbyAlmostDuplicate([500000,800000,1200000],5,400000)






