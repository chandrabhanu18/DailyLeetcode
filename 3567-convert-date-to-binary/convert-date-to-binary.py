class Solution:
    def convertDateToBinary(self, date: str) -> str:
        y=int(date[:4])
        m=int(date[5:7])
        d=int(date[8:])
        y=bin(y)[2:]
        m=bin(m)[2:]
        d=bin(d)[2:]
        answer=str(y)+'-'+str(m)+'-'+str(d)
        return answer
