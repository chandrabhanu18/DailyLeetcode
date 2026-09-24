class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s=str(nums[i])
            total=0
            j=0
            for j in range(len(s)):
                total=total+int(s[j])
                
            if i==total:
                return i
        return -1        