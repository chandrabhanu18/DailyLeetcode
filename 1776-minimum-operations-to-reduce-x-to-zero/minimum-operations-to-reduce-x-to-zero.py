class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        left,right=0,0
        target=sum(nums)-x
        current=0
        maxlen=-1
        if target<0:
            return -1
        if target == 0:
            return len(nums)    
        for right in range(len(nums)):
            current+=nums[right]
            while current>target:
                current-=nums[left]
                left+=1
            if current==target:
                maxlen=max(maxlen,right-left+1)
        if maxlen==-1:
            return -1
        return len(nums)-maxlen   

            
