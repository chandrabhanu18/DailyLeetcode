class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [1] * n

        for segments in range(1, k + 1):
            new_dp = [0] * n
            prefix = 0

            for i in range(n):
                prefix = (prefix + dp[i]) % MOD

                if i > 0:
                    new_dp[i] = (new_dp[i - 1] + prefix - dp[i]) % MOD

            dp = new_dp

        return dp[n - 1]