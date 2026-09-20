class Solution:
    def tribonacci(self, n: int) -> int:
        prev1,prev2,prev3=0,1,1
        if n<=1:
            return n
        for i in range(3,n+1):
            current=prev1+prev2+prev3
            prev1=prev2
            prev2=prev3
            prev3=current
        return prev3        