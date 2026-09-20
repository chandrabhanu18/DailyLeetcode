from collections import Counter
class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        taskcounts=Counter(tasks)
        rounds=0
        for value,count in taskcounts.items():
            if count==1:
                return -1
            rounds+=(count+2)//3
        return rounds         
