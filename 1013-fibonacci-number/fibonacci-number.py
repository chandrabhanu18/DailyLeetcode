class Solution:
    def fib(self, n: int) -> int:
        prev1,prev2=1,2
        if n<=1:
            return n
        for i in range(3,n+1):
            current=prev1+prev2
            prev1=prev2
            prev2=current
        return prev1        