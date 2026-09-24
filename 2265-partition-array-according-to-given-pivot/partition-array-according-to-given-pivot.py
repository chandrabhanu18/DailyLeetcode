class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        # nums.sort()
        l1,l2,p=[],[],[]
        for i in nums:
            if i<pivot:
                l1.append(i)
            elif i>pivot:
                l2.append(i)
            else:
                p.append(i)    
        return l1+p+l2             