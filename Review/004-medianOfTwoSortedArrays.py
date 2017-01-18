
# good solution on leetcode.   basically the same to mine, but a lot more concise.  I avoided using recursive.

# class Solution {
# public:
#     int getkth(int s[], int m, int l[], int n, int k){
#         // let m <= n
#         if (m > n) 
#             return getkth(l, n, s, m, k);
#         if (m == 0)
#             return l[k - 1];
#         if (k == 1)
#             return min(s[0], l[0]);

#         int i = min(m, k / 2), j = min(n, k / 2);
#         if (s[i - 1] > l[j - 1])
#             return getkth(s, m, l + j, n - j, k - j);
#         else
#             return getkth(s + i, m - i, l, n, k - i);
#         return 0;
#     }

#     double findMedianSortedArrays(int A[], int m, int B[], int n) {
#         int l = (m + n + 1) >> 1;
#         int r = (m + n + 2) >> 1;
#         return (getkth(A, m ,B, n, l) + getkth(A, m, B, n, r)) / 2.0;
#     }
# };




import math
class Solution:
	def findMedianSortedArrays(self, arrA, arrB):
		a=len(arrA)
		b=len(arrB)
		med=(a+b)/2
		even=(med*2==(a+b))
		lastRemoved=float('inf')

		
		while (med>0):
			if a==0:
				return ((arrB[b-med-1]+min(arrB[b-med],lastRemoved))/2.0) if even else arrB[b-med-1]
			if b==0:
				return ((arrA[a-med-1]+min(arrA[a-med],lastRemoved))/2.0) if even else arrA[a-med-1]


			if a <= med/2:
				pAIdx=0
				pBIdx=b-med+a
				if arrA[pAIdx] < arrB[pBIdx]:
					b=pBIdx
					lastRemoved=arrB[b] if (arrB[b] < lastRemoved) else lastRemoved
					arrB=arrB[:b]
					med=a


				else:
					return ((arrB[pBIdx-1]+arrB[pBIdx])/2.0 if even else (arrB[pBIdx-1]))

			elif b <= med/2:
				pAIdx=a-med+b
				pBIdx=0
				if arrB[pBIdx] < arrA[pAIdx]:
					a=pAIdx
					lastRemoved=arrA[a] if (arrA[a] < lastRemoved) else lastRemoved
					arrA=arrA[:a]
					med=b


				else:
					return ((arrA[pAIdx-1]+arrA[pAIdx])/2.0 if even else (arrA[pAIdx-1]))
			else:
				pAIdx=int(a-math.ceil(med/2.0))
				pBIdx=int(b-math.ceil(med/2.0))
				if arrA[pAIdx] >= arrB[pBIdx]:
					a=pAIdx
					lastRemoved=arrA[a] if (arrA[a] < lastRemoved) else lastRemoved
					arrA=arrA[:a]
				else:
					b=pBIdx
					lastRemoved=arrB[b] if (arrB[b] < lastRemoved) else lastRemoved
					arrB=arrB[:b]
				med=med/2


		if a==0:
			return ((arrB[b-1]+lastRemoved)/2.0) if even else arrB[b-1]
		if b==0:
			return ((arrA[a-1]+lastRemoved)/2.0) if even else arrA[a-1]

		return ((max(arrA[a-1],arrB[b-1]))+lastRemoved)/2.0 if even else (max(arrA[a-1],arrB[b-1]))

if __name__=="__main__":
	solusion=Solution()
	print(solusion.findMedianSortedArrays([1,6,7,8], [2,3,4,5,9,10]))

