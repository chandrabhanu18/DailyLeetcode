class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        rightmin=[0]*n
        rightmin[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            rightmin[i]=min(rightmin[i+1],nums[i])
        leftmax=nums[0]
        for i in range(n):
            leftmax=max(nums[i],leftmax)
            if leftmax-rightmin[i]<=k:
                return i
        return -1        