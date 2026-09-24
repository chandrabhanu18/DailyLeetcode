class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        n=len(nums) 
        res=[0]*n
        left,right=0,n-1
        for i in range(n):
            if nums[i]<pivot:
                res[left]=nums[i]   
                left+=1
            if nums[n-1-i]>pivot:
                res[right]=nums[n-i-1]
                right-=1
        while left<=right:
            res[left]=pivot
            left+=1
        return res                