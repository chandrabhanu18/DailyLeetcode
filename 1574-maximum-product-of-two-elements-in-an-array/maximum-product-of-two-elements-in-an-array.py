class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest,second=0,0
        for num in nums:
            if num>=largest:
                second=largest
                largest=num
            elif num>second :
                second=num
        return (largest-1)*(second-1)          
