import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        s1=1
        s2=2
        for i in range(3,(2*n)+1):
            if i%2!=0:
                s1+=i
            else:
                s2+=i
        return gcd(s1,s2)