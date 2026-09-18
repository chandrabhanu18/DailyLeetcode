class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        # res=[]
        # for i in order:
        #     for j in friends:
        #         if i==j:
        #             res.append(j)
        # return res
        res=[]
        n=len(order)
        for i in range(n):
            if order[i] in friends:
                res.append(order[i])
        return res