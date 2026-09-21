class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Start a new subarray with just num
            new_dp[num % k] += 1

            # Extend previous subarrays
            for r in range(k):
                if dp[r]:
                    new_r = (r * num) % k
                    new_dp[new_r] += dp[r]

            dp = new_dp

            # Add all subarrays ending here to the answer
            for r in range(k):
                result[r] += dp[r]

        return result