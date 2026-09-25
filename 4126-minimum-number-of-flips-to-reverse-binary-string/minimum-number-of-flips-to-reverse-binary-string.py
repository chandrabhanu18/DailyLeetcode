class Solution:
    def minimumFlips(self, n: int) -> int:
        s = bin(n)[2:]
        flips = 0
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                flips += 2
            left += 1
            right -= 1
            
        return flips