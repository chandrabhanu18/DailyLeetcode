class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        i=j=c=0
        seen=[]
    
        n=len(fruits)
        for i in range(n):
            j=0
            placed=False
            while j<n:
                if j not in seen and fruits[i] <= baskets[j]:
                    seen.append(j)
                    placed=True
                    break
                
                j+=1    

            if not placed:
                c+=1    
            
        return c