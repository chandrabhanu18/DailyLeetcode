class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev1=1
        prev2=2
        if n==1:
            return 1
        for i in range(3,n+1):
            current=prev1+prev2
            prev1=prev2
            prev2=current
        return prev2
