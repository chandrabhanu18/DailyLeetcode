class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # freq={}
        # single_count=[]
        # for i in range(len(nums)-k+1):
        #     new=nums[i:i+k] 
        #     for num in new:
        #         freq[num]=freq.get(num,0)+1

        # for number,count in freq.items():
        #     if freq[number]==1:
        #         single_count.append(number)
        # single_count.sort(reverse=True)
        # if single_count:
        #     return single_count[0]        
        # else:
        #     return -1
        if k==len(nums):
            return max(nums)
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        if k==1:
            answer=-1
            for number,count in freq.items():
                if count==1:
                    answer=max(answer,number)
            return answer
        answer=-1    
        if freq[nums[0]]==1:
            answer=max(answer,nums[0])
        if freq[nums[-1]]==1:
            answer=max(answer,nums[-1])
        return answer                       
