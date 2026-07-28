class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        t=nums1+nums2
        t=sorted(t)
        j=len(t)//2
        if(len(t)%2==0):
            return (t[j]+t[j-1])/2.0
        else:
            return t[j]