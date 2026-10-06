class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed=close_needed=0
        for i in s:
            if i=='(':
                close_needed+=1
            elif i==')':
                if close_needed>0:
                    close_needed-=1
                else:
                    open_needed+=1

        return open_needed+close_needed   