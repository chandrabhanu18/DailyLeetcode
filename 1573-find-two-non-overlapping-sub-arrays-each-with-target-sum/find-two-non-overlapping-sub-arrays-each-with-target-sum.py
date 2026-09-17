class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)

        INF = float('inf')

        # best[i] = minimum length of a target-sum subarray
        # completely inside arr[0...i]
        best = [INF] * n

        left = 0
        curr_sum = 0
        answer = INF

        for right in range(n):
            curr_sum += arr[right]

            # Since all numbers are positive,
            # shrink the window while sum is too large.
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            # We found a subarray [left...right]
            if curr_sum == target:
                length = right - left + 1

                # Need another subarray completely before 'left'
                if left > 0 and best[left - 1] != INF:
                    answer = min(answer, length + best[left - 1])

                # Store the shortest subarray seen so far
                if right == 0:
                    best[right] = length
                else:
                    best[right] = min(best[right - 1], length)

            else:
                # No valid subarray ending at right
                if right > 0:
                    best[right] = best[right - 1]

        return -1 if answer == INF else answer