class Solution:
    def fib(self, n: int) -> int:
        prev1,prev2=0,1
        if n<=1:
            return n
        for i in range(2,n+1):
            current=prev1+prev2
            prev1=prev2
            prev2=current
        return prev2       